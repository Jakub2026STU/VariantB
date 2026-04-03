import numpy as np
from gnuradio import gr

class blk(gr.basic_block):
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='Hamming (7,4) Encoder',
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]

        # Hamming 7,4 berie 4 bity a vyrába 7 bitov
        n_blocks = min(len(in0) // 4, len(out0) // 7)
        if n_blocks == 0:
            return 0

        # Rozsekáme vstup na bloky po 4 bitoch
        in_matrix = in0[:n_blocks*4].reshape((n_blocks, 4))
        d1 = in_matrix[:, 0]
        d2 = in_matrix[:, 1]
        d3 = in_matrix[:, 2]
        d4 = in_matrix[:, 3]

        # Výpočet paritných bitov
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4

        # Zostavenie 7-bitového Hammingovho slova: p1, p2, d1, p3, d2, d3, d4
        out_matrix = np.column_stack((p1, p2, d1, p3, d2, d3, d4))
        out0[:n_blocks*7] = out_matrix.flatten()

        # Povieme GNU Radiu, koľko bitov sme spotrebovali a koľko vyrobili
        self.consume(0, n_blocks * 4)
        return n_blocks * 7