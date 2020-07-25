# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:00:39 2020

@author: Administrator
"""

import pandas as pd                         #导入pandas包
ratings = pd.read_csv(r'E:\推荐\ml-latest-small\ratings.csv')    
print (ratings.head(20))