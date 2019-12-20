#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:23:05 2019

@author: salman
"""
import pandas as pd
names = ["dengue.csv", "dengue2018.csv", "denguuuu.csv", "indluenza2018.csv", "malaa.csv", "malaria.csv"]
final_data_csv = pd.DataFrame(columns = ["",'date','tweet','hashtags','place'])

for name in names:
    
    data = pd.read_csv(name)
    sample = data.loc[:,['date','tweet','hashtags','place']]
    #sample.to_csv(name.split('.')[0] + "Final.csv", index = False)
    final_data_csv = pd.concat([final_data_csv, sample], axis = 0)
final_data_csv.to_csv("Final_data.csv", index = False)