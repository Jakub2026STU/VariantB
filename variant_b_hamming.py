#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: MPSK channel with Noise and Hamming Encoding
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import fec
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading
import variant_b_hamming_epy_block_0 as epy_block_0  # embedded python block
import variant_b_hamming_epy_block_1 as epy_block_1  # embedded python block
import variant_b_hamming_modulation_config as modulation_config  # embedded python module


def snipfcn_snippet_0(self):
    from PyQt5 import QtWidgets

    # Apply a custom font size to all widgets
    app = QtWidgets.QApplication.instance()
    if app is not None:
        app.setStyleSheet("QWidget { font-size: 22px; }")  # Adjust size


def snippets_main_after_init(tb):
    snipfcn_snippet_0(tb)

class variant_b_hamming(gr.top_block, Qt.QWidget):

    def __init__(self, modulation_name='QPSK'):
        gr.top_block.__init__(self, "MPSK channel with Noise and Hamming Encoding", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MPSK channel with Noise and Hamming Encoding")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "variant_b_hamming")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Parameters
        ##################################################
        self.modulation_name = modulation_name

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6
        self.modulation = modulation = digital.constellation_calcdist(modulation_config.get_constellation(modulation_name), modulation_config.get_symbol_map(modulation_name),
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.modulation.set_npwr(1.0)

        ##################################################
        # Blocks
        ##################################################

        self.measurement_control_0 = Qt.QTabWidget()
        self.measurement_control_0_widget_0 = Qt.QWidget()
        self.measurement_control_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.measurement_control_0_widget_0)
        self.measurement_control_0_grid_layout_0 = Qt.QGridLayout()
        self.measurement_control_0_layout_0.addLayout(self.measurement_control_0_grid_layout_0)
        self.measurement_control_0.addTab(self.measurement_control_0_widget_0, 'BER MPSK')
        self.top_grid_layout.addWidget(self.measurement_control_0, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("BER Output without Hamming Encoding")

        labels = ['BER', 'BER', 'Total Bits', '', '',
            '', '', '', '', '']
        units = ['= X', '= X', 'bits', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("blue", "red"), ("black", "white"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.qwidget(), Qt.QWidget)
        self.measurement_control_0_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.measurement_control_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.measurement_control_0_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("BER Output with Hamming Encoding")

        labels = ['BER', 'BER', 'Total Bits', '', '',
            '', '', '', '', '']
        units = ['= X', '= X', 'bits', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("blue", "red"), ("black", "white"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.qwidget(), Qt.QWidget)
        self.measurement_control_0_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.measurement_control_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.measurement_control_0_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
            5000,
            10,
            0.95,
            1.2,
            'MPSK Error Rate Histogram: Hamming Code vs. No ECC',
            2,
            None # parent
        )

        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0.enable_grid(True)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)


        labels = ['Uncoded MPSK', 'Hamming Code MPSK', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["red", "blue", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [0, 3, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [0.8, 1, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_histogram_sink_x_0_win, 3, 1, 2, 1)
        for r in range(3, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            'Comparison of MPSK Signal Constellations: Noise-Free vs. Noise-Affected', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['Noise-Affected MPSK', 'Noise-Free MPSK', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["red", "blue", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 3, 0, 2, 1)
        for r in range(3, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fec_ber_bf_0_0 = fec.ber_bf(False, 100, -7.0)
        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
        self.epy_block_1 = epy_block_1.blk()
        self.epy_block_0 = epy_block_0.blk()
        self.digital_constellation_encoder_bc_0_0 = digital.constellation_encoder_bc(modulation)
        self.digital_constellation_encoder_bc_0 = digital.constellation_encoder_bc(modulation)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(modulation)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(modulation)
        self.blocks_unpacked_to_packed_xx_0_1_0 = blocks.unpacked_to_packed_bb(modulation.bits_per_symbol(), gr.GR_MSB_FIRST)
        self.blocks_unpacked_to_packed_xx_0_1 = blocks.unpacked_to_packed_bb(modulation.bits_per_symbol(), gr.GR_MSB_FIRST)
        self.blocks_unpacked_to_packed_xx_0_0 = blocks.unpacked_to_packed_bb(modulation.bits_per_symbol(), gr.GR_MSB_FIRST)
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(modulation.bits_per_symbol(), gr.GR_MSB_FIRST)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(1, modulation.bits_per_symbol(), "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(modulation.bits_per_symbol(), 1, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(modulation.bits_per_symbol(), 1, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, modulation.bits_per_symbol(), "", False, gr.GR_LSB_FIRST)
        self.blocks_char_to_float_0_0_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(0.1)
        self.blocks_abs_xx_0_0 = blocks.abs_ff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, (2**modulation.bits_per_symbol()), 10000))), True)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, modulation_config.calculate_noise("QPSK",9,7), 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, modulation_config.calculate_noise("QPSK",9,4), 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_unpacked_to_packed_xx_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_unpacked_to_packed_xx_0_1_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_encoder_bc_0_0, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.blocks_abs_xx_0_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_histogram_sink_x_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_char_to_float_0_0_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_char_to_float_0_0_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_char_to_float_0_0_1_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_constellation_encoder_bc_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_char_to_float_0_0_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_unpacked_to_packed_xx_0_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_abs_xx_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_char_to_float_0_0_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.fec_ber_bf_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0_0, 0), (self.fec_ber_bf_0, 1))
        self.connect((self.blocks_unpacked_to_packed_xx_0_1, 0), (self.fec_ber_bf_0_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0_1_0, 0), (self.fec_ber_bf_0_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.qtgui_const_sink_x_0_0, 1))
        self.connect((self.digital_constellation_encoder_bc_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.epy_block_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.fec_ber_bf_0_0, 0), (self.qtgui_number_sink_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "variant_b_hamming")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_modulation_name(self):
        return self.modulation_name

    def set_modulation_name(self, modulation_name):
        self.modulation_name = modulation_name

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)

    def get_modulation(self):
        return self.modulation

    def set_modulation(self, modulation):
        self.modulation = modulation
        self.digital_constellation_decoder_cb_0.set_constellation(self.modulation)
        self.digital_constellation_decoder_cb_0_0.set_constellation(self.modulation)
        self.digital_constellation_encoder_bc_0.set_constellation(self.modulation)
        self.digital_constellation_encoder_bc_0_0.set_constellation(self.modulation)



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--modulation-name", dest="modulation_name", type=str, default='QPSK',
        help="Set Modulation Name [default=%(default)r]")
    return parser


def main(top_block_cls=variant_b_hamming, options=None):
    if options is None:
        options = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(modulation_name=options.modulation_name)
    snippets_main_after_init(tb)
    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
