#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:22:45 2019

@author: salman
"""

import re
import pandas as pd
data = pd.read_csv('data.csv', encoding = 'unicode_escape')
s = "I love #stackoverflow because #people are very #helpful!"
re.findall(r"#(\w+)", s)

for i in range(data.shape[0]):
    s = data['tweet'][i]
    hashtag = re.findall(r"#(\w+)", s)
    data['hashtag'][i] = hashtag