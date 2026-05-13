import numpy as np
from gnuradio import gr

class blk(gr.basic_block):
    def __init__(self):
        gr.basic_block.__init__(self, name='Hamming (7,4) Decoder',
            in_sig=[np.uint8], out_sig=[np.uint8])

    def general_work(self, input_items, output_items):
        in0, out0 = input_items[0], output_items[0]
        n_blocks = min(len(in0) // 7, len(out0) // 4)
        if n_blocks == 0: return 0

        in_matrix = in0[:n_blocks*7].copy().reshape((n_blocks, 7))
        p1, p2, d1, p3, d2, d3, d4 = [in_matrix[:, i] for i in range(7)]

        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4
        syndrome = s1 * 1 + s2 * 2 + s3 * 4

        for i in range(n_blocks):
            if syndrome[i] > 0:
                in_matrix[i, syndrome[i] - 1] ^= 1

        out_matrix = np.column_stack((in_matrix[:,2], in_matrix[:,4], in_matrix[:,5], in_matrix[:,6]))
        out0[:n_blocks*4] = out_matrix.flatten()
        self.consume(0, n_blocks * 7)
        return n_blocks * 4