# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib
import matplotlib.pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
from matplotlib import rc
from matplotlib.dates import date2num
from matplotlib.pyplot import savefig

def draw_xkcd(xx, yy, xlabel, ylabel, olabel):
	"""
		xx is a date list
	"""
	pl.xkcd()
	matplotlib.rc('font', family='Arial')
	ax = pl.axes()
	x = np.array([date2num(vv) for vv in xx])
	y = np.array(yy)
	#ax.plot(x, y, 'b', lw=1, label=olabel)
	pl.bar(x, y)
	ax.set_title(olabel)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.set_xlim(min(xx), max(xx))
	ax.set_ylim(0, max(yy))
	fig = matplotlib.pyplot.gcf()
	fig.set_size_inches(24,12)
	fig.savefig(olabel+'.png',dpi=120)
	pl.clf()