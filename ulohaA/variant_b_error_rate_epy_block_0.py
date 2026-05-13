import numpy as np
from gnuradio import gr

class blk(gr.basic_block):
    def __init__(self, frame_size=100, bits_per_symbol=4):
        gr.basic_block.__init__(
            self,
            name='Error Rate Counter',
            in_sig=[np.uint8, np.uint8], # in0: Truth (čisté), in1: Received (šum)
            out_sig=[np.float32, np.float32, np.float32] # SER, BER, FER
        )
        self.frame_size = frame_size
        self.bits_per_symbol = bits_per_symbol
        self.total_bits = 0
        self.bit_errors = 0
        self.total_symbols = 0
        self.symbol_errors = 0
        self.total_frames = 0
        self.frame_errors = 0

    def general_work(self, input_items, output_items):
        # V tomto zapojení sú oba vstupy bajty (0-255)
        in_truth = input_items[0]
        in_noisy = input_items[1]
        
        n_input = min(len(in_truth), len(in_noisy))
        n_frames = n_input // self.frame_size
        
        if n_frames == 0:
            return 0

        # Spracujeme dáta po celých rámcoch
        data_len = n_frames * self.frame_size
        t = in_truth[:data_len]
        r = in_noisy[:data_len]

        # 1. BER (Bit Error Rate) - rozbalíme bajty na bity a porovnáme
        t_bits = np.unpackbits(t)
        r_bits = np.unpackbits(r)
        self.bit_errors += np.sum(t_bits != r_bits)
        self.total_bits += len(t_bits)

        # 2. SER (Symbol Error Rate) - pre 16-QAM (4 bity na symbol)
        # Každý bajt má 2 symboly (horný a dolný nibble)
        t_high, t_low = (t >> 4) & 0x0F, t & 0x0F
        r_high, r_low = (r >> 4) & 0x0F, r & 0x0F
        self.symbol_errors += np.sum(t_high != r_high) + np.sum(t_low != r_low)
        self.total_symbols += len(t) * 2

        # 3. FER (Frame Error Rate)
        t_frames = t.reshape(-1, self.frame_size)
        r_frames = r.reshape(-1, self.frame_size)
        # Rámec je chybný, ak sa v ňom líši aspoň jeden bajt
        self.frame_errors += np.sum(np.any(t_frames != r_frames, axis=1))
        self.total_frames += n_frames

        # Výpočet logaritmov pre GUI (Number Sink)
        # Ak je chyba 0, vrátime -10.0 (predstavuje log10 od veľmi malého čísla)
        ser = self.symbol_errors / self.total_symbols if self.total_symbols > 0 else 1e-10
        ber = self.bit_errors / self.total_bits if self.total_bits > 0 else 1e-10
        fer = self.frame_errors / self.total_frames if self.total_frames > 0 else 1e-10

        output_items[0][:] = np.log10(ser) if ser > 0 else -10.0
        output_items[1][:] = np.log10(ber) if ber > 0 else -10.0
        output_items[2][:] = np.log10(fer) if fer > 0 else -10.0

        self.consume(0, data_len)
        self.consume(1, data_len)
        return len(output_items[0])