import numpy as np
from gnuradio import gr

class blk(gr.basic_block):
    def __init__(self):
        gr.basic_block.__init__(
            self,
            name='Hamming (7,4) Decoder',
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]

        # Dekóder berie 7 bitov a vyťahuje z nich 4 čisté bity
        n_blocks = min(len(in0) // 7, len(out0) // 4)
        if n_blocks == 0:
            return 0

        # Skopírujeme dáta do matice (musí byť copy, lebo in0 je read-only)
        in_matrix = in0[:n_blocks*7].copy().reshape((n_blocks, 7))
        
        p1 = in_matrix[:, 0]
        p2 = in_matrix[:, 1]
        d1 = in_matrix[:, 2]
        p3 = in_matrix[:, 3]
        d2 = in_matrix[:, 4]
        d3 = in_matrix[:, 5]
        d4 = in_matrix[:, 6]

        # Výpočet syndrómu (slúži na odhalenie toho, kde nastala chyba)
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4

        syndrome = s1 * 1 + s2 * 2 + s3 * 4

        # Oprava jednej chyby pre každý prijatý 7-bitový blok
        for i in range(n_blocks):
            syn = syndrome[i]
            if syn > 0:
                # Ak syndróm nie je 0, ukazuje presne na index pokazeného bitu (1-based, preto -1)
                in_matrix[i, syn - 1] ^= 1

        # Vytiahnutie správnych/opravených dátových bitov
        d1_c = in_matrix[:, 2]
        d2_c = in_matrix[:, 4]
        d3_c = in_matrix[:, 5]
        d4_c = in_matrix[:, 6]

        out_matrix = np.column_stack((d1_c, d2_c, d3_c, d4_c))
        out0[:n_blocks*4] = out_matrix.flatten()

        self.consume(0, n_blocks * 7)
        return n_blocks * 4
