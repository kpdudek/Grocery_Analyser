# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:21:52 2018

@author: kpdud
"""

import csv
import math
import numpy as np

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
    
    