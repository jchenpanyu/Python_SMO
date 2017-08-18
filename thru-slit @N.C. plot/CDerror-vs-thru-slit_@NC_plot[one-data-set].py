# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:04:34 2017

Created on Thu Mar 16 11:46:17 2017
read and plot CD error vs. Zernike per cutline
vai DataFrame

@author: vincchen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = r'./'
file_name = 'PC-SMO_data.xlsx'

data = pd.read_excel(path + file_name)
data = data.drop(['del'], axis=1)

data['CD error'] = data['IPE1'] + data['IPE2']
data['absolute CD error'] = np.abs(data['CD error'] )

data_rows, data_columns = data.shape[0], data.shape[1]
# <slitlocs>-10600/-8480/-6360/-4240/-2120/0/2120/4240/6360/8480/10600</slitlocs>
# delta_slit = 2.12
n_slit = 11
n_cutline = 33 # data_rows/n_slit

cutline_group = []
for i in np.arange(n_cutline):
    cutline_group.append(data['Cutline'][i*n_slit+1])

max_CDerror_thruslit = []
for i in np.arange(n_cutline):
    max_CDerror_thruslit.append(np.max(data['absolute CD error'][i * n_slit : (i+1) * n_slit]))

H_index = [0, 2, 4, 6, 16, 18, 20, 22]
V_index = [1, 3, 5, 7, 17, 19, 21, 23]
H_CDerror = []
V_CDerror = []
for i in H_index:
    H_CDerror.append(max_CDerror_thruslit[i])
for i in V_index:
    V_CDerror.append(max_CDerror_thruslit[i])

fig = plt.figure(figsize=(14, 6))
x_label = ['-1', '0', '1', '2', '7', '8', '9', '10']
y_max = np.max([np.max(H_CDerror), np.max(V_CDerror)])
# horizontal plot
ax_1 = plt.subplot(1,2,1)
ax_1.bar(np.arange(len(H_CDerror)), H_CDerror, fc='black', tick_label = x_label, align='center')
plt.ylim((0, (y_max*11).round()/10))
plt.xlabel('Critical Pattern', fontsize=15)
plt.ylabel('absolute Max CD error(nm)', fontsize=15)
plt.title('absolute value of thru-slit Max CD error(Horizontal)')
# vertical plot
ax_2 = plt.subplot(1,2,2)
ax_2.bar(np.arange(len(V_CDerror)), V_CDerror, fc='black', tick_label = x_label, align='center')
plt.ylim((0, (y_max*11).round()/10))
plt.xlabel('Critical Pattern', fontsize=15)
plt.ylabel('absolute Max CD error(nm)', fontsize=15)
plt.title('absolute value of thru-slit Max CD error(Vertical)')
