import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, restart=False, tag_key='packet_len'):
        gr.sync_block.__init__(
            self,
            name='FER',
            in_sig=[np.uint8, np.uint8],
            out_sig=[np.float32]
        )
    def work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
        return len(output_items[0])
