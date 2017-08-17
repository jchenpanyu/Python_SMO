# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:35:17 2017

run time analysis
$job_ID$/h/work/tachyonjob/host/summary.xml

@author: vincchen
"""

import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

xml_file = ET.ElementTree(file='17_CTM+_summary.xml')
xml_root = xml_file.getroot()

stage = []
time = []

for xml_stage in xml_root:
    for xml_stage_enable, xml_stage_time in zip(xml_stage.iter(tag='enable'), xml_stage.iter(tag='time')):
        stage.append(xml_stage_enable.text)
        time.append(float(xml_stage_time.text))

fig = plt.figure(figsize=((int(len(stage)), 6)))
plt.bar(np.arange(len(time)), time, fc='black', tick_label = stage, align='center')
plt.tick_params(labelsize=15)
for a, b in zip(np.arange(len(time)), time):
    plt.text(a, b, '%.f' % b, horizontalalignment='center', verticalalignment= 'bottom',fontsize=12)
plt.xlim((-1, len(stage)))
plt.yscale('log')
plt.xlabel('stage', fontsize=20)
plt.ylabel('time(s)', fontsize=20)
plt.show()