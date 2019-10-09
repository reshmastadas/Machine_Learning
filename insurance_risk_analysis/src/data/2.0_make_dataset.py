import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

# Creating path variable to read train data
RAW_DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','raw'))

# Creating package path
PACKAGE_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,'packages'))

# adding package path to path variable
sys.path.insert(1, PACKAGE_PATH)

print('Reading train.csv...')
df = pd.read_csv(os.path.join(RAW_DATA_PATH,'train.csv'))
print('Reading done.')

print('Performing stratified split on train data')
split = StratifiedShuffleSplit(n_splits=1,test_size=0.25,random_state=42)

for train_index, test_index in split.split(df,df['Claim']):
    train_set = df.iloc[train_index]
    test_set = df.iloc[test_index]
print('Splitting done.')

print('Storing dataframes into csv')
train_set.to_csv(os.path.join(RAW_DATA_PATH,'train_set.csv'))
test_set.to_csv(os.path.join(RAW_DATA_PATH,'test_set.csv'))
print('Procedure complete.')