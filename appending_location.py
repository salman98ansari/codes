#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:08:27 2019

@author: salman
"""

import pandas as pd
import numpy as np
name = pd.read_csv("name.csv")
name = name.dropna(how = 'all')
lst_city = [x.split('[')[0] for x in name[' City ']]
lst_state = [x for x in name[' State']]


data = pd.read_csv("Final_data.csv").values
for i in range(data.shape[0]):
    data[i][3] = np.random.choice(lst_city)
    
pd.DataFrame(data).to_csv("Final_data_with_location.csv", index = False)

data = pd.read_csv("Final_data_with_location.csv")
data['state'] = 'NaN'
data = data.values
for i in range(data.shape[0]):
    index = lst_city.index(data[i][3])
    data[i][4] = lst_state[index]
pd.DataFrame(data).to_csv("Final_data_with_location.csv", index = False)
