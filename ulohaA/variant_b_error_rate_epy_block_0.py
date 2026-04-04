import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, frame_size=1024, bits_per_symbol=4):
        gr.sync_block.__init__(
            self,
            name='Error Rate Counter',
            in_sig=[np.uint8, np.uint8],
            out_sig=[np.float32, np.float32, np.float32]
        )
        self.frame_size = frame_size
        self.bits_per_symbol = bits_per_symbol

        self.total_bits = 0
        self.bit_errors = 0
        self.total_symbols = 0
        self.symbol_errors = 0
        self.total_frames = 0
        self.frame_errors = 0

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]

        if len(in0) == 0 or len(in1) == 0:
            return 0

        n = min(len(in0), len(in1))
        in0 = in0[:n]
        in1 = in1[:n]

        # Vypocet FER
        byte_errors = np.sum(in0 != in1)
        self.total_frames += 1
        if byte_errors > 0:
            self.frame_errors += 1

        # Vypocet BER (rozbalenie bajtov na bity)
        bits0 = np.unpackbits(in0)
        bits1 = np.unpackbits(in1)
        self.bit_errors += np.sum(bits0 != bits1)
        self.total_bits += len(bits0)

        # Vypocet SER pre 16-QAM (1 bajt = 2 symboly po 4 bitoch)
        sym0_h = (in0 >> 4) & 0x0F
        sym0_l = in0 & 0x0F
        sym1_h = (in1 >> 4) & 0x0F
        sym1_l = in1 & 0x0F
        self.symbol_errors += np.sum(sym0_h != sym1_h) + np.sum(sym0_l != sym1_l)
        self.total_symbols += n * 2

        # Vypocet logaritmov (s poistkou -10 proti padnutiu pri nule)
        ber = self.bit_errors / self.total_bits if self.total_bits > 0 else 0
        ser = self.symbol_errors / self.total_symbols if self.total_symbols > 0 else 0
        fer = self.frame_errors / self.total_frames if self.total_frames > 0 else 0

        ber_log = np.log10(ber) if ber > 0 else -10.0
        ser_log = np.log10(ser) if ser > 0 else -10.0
        fer_log = np.log10(fer) if fer > 0 else -10.0

        # Zapis na vystupy
        output_items[0][:] = ser_log
        output_items[1][:] = ber_log
        output_items[2][:] = fer_log

        return n
