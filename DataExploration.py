#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:32:14 2019

@author: leealex
"""

import pandas as pd
import warnings
import os
import sys, getopt

def main(argv):
    if len(argv) < 2:
        print("Directory name needs to be specified.")
        sys.exit()
    elif argv[1] != "-d":
        print("Directory name flag should be '-d'.")
        sys.exit()
    elif len(argv) == 2:
        print("Data directory needs to be specified.")
        sys.exit()
    
    directory_name = argv[2]         
    
    cwd = os.getcwd() # current directory
    try:
        train = pd.read_csv(cwd + '/' + directory_name + '/train.csv')
        test = pd.read_csv(cwd + '/' + directory_name + '/test.csv')
    except:
        print("Either training file or test file doesn't exist. Please try to save file in the format of 'train.csv' and 'test.csv' format. ")
        sys.exit()
    
        
if __name__ == "__main__":
    main(sys.argv)