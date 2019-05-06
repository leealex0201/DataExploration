#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:32:14 2019

@author: leealex
"""

import pandas as pd
import warnings
import os

warnings.filterwarnings("ignore")

cwd = os.getcwd()
train = pd.read_csv(cwd + '/Titanic/train.csv')
test = pd.read_csv(cwd + '/Titanic/test.csv')
