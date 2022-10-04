#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:36:48 2022

@author: ekenee
"""

import csv
import os


#Reads files
with open("/Users/ekenee/Desktop/untitled folder/makeup.csv", encoding='utf-8') as f:
    f_csv = csv.reader(f) 
    headers = next(f_csv) 
    for row in f_csv:
        print(row[0])
        


header = ['Name', 'Position', 'Age']
rows = [('Lebron', 'SF', '37'),
        ('James Harden', 'SG', '34'),
        ('KD', 'SF', '32')]

#Writes data into files
with open('/Users/ekenee/Desktop/untitled folder/newfile.csv','w') as f: 
    f_csv = csv.writer(f) 
    f_csv.writerow(headers) 
    f_csv.writerows(rows)