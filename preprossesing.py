# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:40:55 2019

@author: Barry
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('train.csv' ,encoding='UTF-8')

dn = df.isnull().any()
print(dn)
type(dn)