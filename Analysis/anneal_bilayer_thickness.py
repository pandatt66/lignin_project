#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:52:50 2017

@author: xtong3
"""

import matplotlib.pylab as plt
from read_xvg import read_xvg
import my_plot_settings_article as mpsa
import argparse
import numpy as np
from scipy.signal import savgol_filter


parser = argparse.ArgumentParser()

parser.add_argument('sys_name')
parser.add_argument('T_start')
parser.add_argument('T_end')
parser.add_argument('xvg_files', nargs='+')

args = parser.parse_args()

# Bilayer thickness is defined from P-P distance

T_start = args.T_start
T_end = args.T_end
sys_name = args.sys_name
xvg_files = args.xvg_files

# P atom coodinates on each leaflet
P_upper= read_xvg(xvg_files[0])

P_lower=read_xvg(xvg_files[1])

bilayer_thickness =np.column_stack((P_upper[:,0], P_upper[:,1]-P_lower[:,1]))

np.savetxt('thickness_'+sys_name+ '.xvg',bilayer_thickness )


#bilayer_thickness_filtered= savgol_filter(bilayer_thickness[:,1], 101, 2)

Temp =np.linspace(int(T_start), int(T_end), num=len(P_upper))

plt.plot(Temp, bilayer_thickness)

plt.xlim(250, 360)

plt.ylim(3.3, 3.6)

mpsa.axis_setup('x')
mpsa.axis_setup('y')

plt.legend() 
plt.xlabel('T (K)',labelpad=mpsa.axeslabelpad)
plt.ylabel('Bilayer Thickness (nm)',labelpad=mpsa.axeslabelpad)
mpsa.save_figure('thickness_'+sys_name + '.png')
plt.show()



