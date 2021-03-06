#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: fmReceiver3
# Generated: Tue Apr  5 12:54:17 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class fmReceiver3(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="fmReceiver3")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2000000
        self.freq = freq = 99.3e6

        ##################################################
        # Blocks
        ##################################################
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=88e6,
        	maximum=120e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot original",
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.rtlsdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_1.set_sample_rate(samp_rate)
        self.rtlsdr_source_1.set_center_freq(freq, 0)
        self.rtlsdr_source_1.set_freq_corr(0, 0)
        self.rtlsdr_source_1.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_1.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_1.set_gain_mode(False, 0)
        self.rtlsdr_source_1.set_gain(49.2, 0)
        self.rtlsdr_source_1.set_if_gain(20, 0)
        self.rtlsdr_source_1.set_bb_gain(20, 0)
        self.rtlsdr_source_1.set_antenna("", 0)
        self.rtlsdr_source_1.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=500,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 1e5, 1e6, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, 54e3, 60e3, 3e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, 18.5e3, 19.5e3, 3e3, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=5e5,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.band_pass_filter_0_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 2))    
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_xx_0, 3))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.rtlsdr_source_1, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rtlsdr_source_1, 0), (self.wxgui_waterfallsink2_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e5, 1e6, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, 54e3, 60e3, 3e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 18.5e3, 19.5e3, 3e3, firdes.WIN_HAMMING, 6.76))
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_1.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.rtlsdr_source_1.set_center_freq(self.freq, 0)


def main(top_block_cls=fmReceiver3, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
