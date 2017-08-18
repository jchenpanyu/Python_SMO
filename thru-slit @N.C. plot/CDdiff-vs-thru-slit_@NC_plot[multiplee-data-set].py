# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:03:43 2017

CD diff. vs. Zernike per cutline thru-slit

@author: vincchen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = r'./'
file_name_list = ['PC-SMO_data_1.xlsx', 'PC-SMO_data_2.xlsx','PC-SMO_data_3.xlsx']

# <slitlocs>-10600/-8480/-6360/-4240/-2120/0/2120/4240/6360/8480/10600</slitlocs>
# delta_slit = 2.12
n_slit = 11
n_cutline = 33
# symmetric pattern set
H_SymmetricPattern_set = zip([0, 2, 16, 18], [6, 4, 22, 20])
V_SymmetricPattern_set = zip([1, 3, 17, 19], [7, 5, 23, 21])

H_CDdiff_set = np.zeros((len(file_name_list), len(H_SymmetricPattern_set)))
V_CDdiff_set = np.zeros((len(file_name_list), len(V_SymmetricPattern_set)))

for file_name, n in zip(file_name_list, np.arange(len(file_name_list))):
    data = pd.read_excel(path + file_name)
    data = data.drop(['del'], axis=1)

    for i in np.arange(len(H_SymmetricPattern_set)):
        H_index = H_SymmetricPattern_set[i]
        V_index = V_SymmetricPattern_set[i]
        H_CDdiff_set[n][i] = np.max( np.abs( data['Exposure CD'][H_index[0]*n_slit : (H_index[0]+1)*n_slit].values - data['Exposure CD'][H_index[1]*n_slit : (H_index[1]+1)*n_slit].values ))
        V_CDdiff_set[n][i] = np.max( np.abs( data['Exposure CD'][V_index[0]*n_slit : (V_index[0]+1)*n_slit].values - data['Exposure CD'][V_index[1]*n_slit : (V_index[1]+1)*n_slit].values ))
    
 
fig = plt.figure(figsize=(14, 6))
x_label = ['-1-2', '0-1', '7-10', '8-9']
y_max = np.max([np.max(H_CDdiff_set), np.max(V_CDdiff_set)])
color_map = ['black', 'red', 'blue']
# bar的参数
total_barwidth = 0.8
number_bar = len(file_name_list)
bar_width = total_barwidth / number_bar
x = np.arange(len(H_SymmetricPattern_set)) - (total_barwidth - bar_width)/3

# horizontal plot
ax_1 = plt.subplot(1,2,1)
ax_1.yaxis.grid(True)
plt.ylim((0, (y_max*11).round()/10))
plt.xlabel('Critical Pattern Set', fontsize=15)
plt.ylabel('absolute Max CD Diff(nm)', fontsize=15)
plt.title('absolute value of thru-slit Max CD Diff(Horizontal)')
for i, j in zip(np.arange(len(file_name_list)), color_map):
    ax_1.bar(x+i*bar_width, H_CDdiff_set[i], width=bar_width, fc=j, tick_label=x_label, align='edge')

# vertical plot
ax_2 = plt.subplot(1,2,2)
ax_2.yaxis.grid(True)
plt.ylim((0, (y_max*11).round()/10))
plt.xlabel('Critical Pattern Set', fontsize=15)
plt.ylabel('absolute Max CD Diff(nm)', fontsize=15)
plt.title('absolute value of thru-slit Max CD Diff(Vertical)')
for i, j in zip(np.arange(len(file_name_list)), color_map):
    ax_2.bar(x + i*bar_width, V_CDdiff_set[i], width=bar_width, fc=j, tick_label=x_label, align='edge')

plt.show()