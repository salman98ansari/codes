# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import ast

data = pd.read_csv('data.csv' , encoding = 'unicode_escape')
data['hashtag'] = data.hashtag.apply(lambda s: list(ast.literal_eval(s)))
cities = list(data['city'].unique())
for i in range(2):
    cities.pop()
    
polar = []
for city in cities:
    dengue_count = 0
    malaria_count = 0
    influenza_count = 0
    zika_count = 0
    chiken_count = 0
    other = 0
    check =  data.loc[data['city'] == city]
    pos = check.loc[check['polar'] == 'pos'].shape[0]
    neg = check.loc[check['polar'] == 'neg'].shape[0]
    lst = list(check['Unnamed: 0'])
    for i in lst:
        if ('malaria' in check['hashtag'][i] or 'Malaria' in check['hashtag'][i]):
            malaria_count += 1
        if ('zika' in check['hashtag'][i] or 'Zika' in check['hashtag'][i] or 'ZikaVirus' in check['hashtag'][i] or 'zikavirus' in check['hashtag'][i]):
            zika_count += 1
        if ('dengue' in check['hashtag'][i] or 'Dengue' in check['hashtag'][i]):
            dengue_count += 1
        if ('chicungunya' in check['hashtag'][i] or 'Chicungunya' in check['hashtag'][i]):
            chiken_count += 1
        if ('influenza' in check['hashtag'][i] or 'Influenza' in check['hashtag'][i]):
            influenza_count += 1
        else:
            other += 1
    total = pos + neg
    pos = int(((pos + neg) * 30)/100)
    
    if(pos < neg):
        polar.append('Epedimic')
        x = 'Epedimic'
    else:
        polar.append('Non Epedimic')
        x = 'Non Epedimic'
    print(city + "------>" + x, total, pos, neg, malaria_count, dengue_count)
    

    
