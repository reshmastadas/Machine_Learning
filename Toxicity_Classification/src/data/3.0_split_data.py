import pandas as pd
import os
import sys

# prepare data path to read data
RAW_DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','raw'))
# prepare package path to get functions commonly used
PACKAGE_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,os.path.pardir,'Common_Functions','split_data'))

# add PACKAGE_PATH to path
sys.path.insert(0,PACKAGE_PATH)

from train_test_validation import SplitData as ttv

# read csv
shopint_df = pd.read_csv(os.path.join(RAW_DATA_PATH,'online_shoppers_intention.csv'))

split = ttv()
train_df,validation_df,test_df = split.fit_transform(shopint_df)

train_df.to_csv(os.path.join(RAW_DATA_PATH,'train_df.csv'))

validation_df.to_csv(os.path.join(RAW_DATA_PATH,'validation_df.csv'))
test_df.to_csv(os.path.join(RAW_DATA_PATH,'test_df.csv'))