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
file_name = 'PC-SMO_data.xlsx'

data = pd.read_excel(path + file_name)
data = data.drop(['del'], axis=1)

# <slitlocs>-10600/-8480/-6360/-4240/-2120/0/2120/4240/6360/8480/10600</slitlocs>
# delta_slit = 2.12
n_slit = 11
n_cutline = 33
# symmetric pattern set
H_SymmetricPattern_set = zip([0, 2, 16, 18], [6, 4, 22, 20])
V_SymmetricPattern_set = zip([1, 3, 17, 19], [7, 5, 23, 21])


H_CDdiff_set = []
V_CDdiff_set = []

for i in np.arange(len(H_SymmetricPattern_set)):
    H_index = H_SymmetricPattern_set[i]
    V_index = V_SymmetricPattern_set[i]
    H_CDdiff_set.append( np.max( np.abs( data['Exposure CD'][H_index[0]*n_slit : (H_index[0]+1)*n_slit].values - data['Exposure CD'][H_index[1]*n_slit : (H_index[1]+1)*n_slit].values )))
    V_CDdiff_set.append( np.max( np.abs( data['Exposure CD'][V_index[0]*n_slit : (V_index[0]+1)*n_slit].values - data['Exposure CD'][V_index[1]*n_slit : (V_index[1]+1)*n_slit].values )))
    
    
fig = plt.figure(figsize=(14, 6))
x_label = ['-1-2', '0-1', '7-10', '8-9']
y_max = np.max([np.max(H_CDdiff_set), np.max(V_CDdiff_set)])
# horizontal plot
ax_1 = plt.subplot(1,2,1)
ax_1.bar(np.arange(len(H_CDdiff_set)), H_CDdiff_set, fc='black', tick_label = x_label, align='center')
plt.ylim((0, (y_max*11).round()/10))
plt.xlabel('Critical Pattern Set', fontsize=15)
plt.ylabel('absolute Max CD Diff(nm)', fontsize=15)
plt.title('absolute value of thru-slit Max CD Diff(Horizontal)')
# vertical plot
ax_2 = plt.subplot(1,2,2)
ax_2.bar(np.arange(len(V_CDdiff_set)), V_CDdiff_set, fc='black', tick_label = x_label, align='center')
plt.ylim((0, (y_max*11).round()/10))
plt.xlabel('Critical Pattern Set', fontsize=15)
plt.ylabel('absolute Max CD Diff(nm)', fontsize=15)
plt.title('absolute value of thru-slit Max CD Diff(Vertical)')




