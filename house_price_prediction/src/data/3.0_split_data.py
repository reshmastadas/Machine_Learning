import os
import sys
import pandas as pd
import hashlib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.base import BaseEstimator, TransformerMixin

PACKAGE_PATH =  os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,os.path.pardir,
                                            'Common_Functions','split_data'))
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'data','raw'))

INTERIM_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'data','interim'))

sys.path.insert(1, PACKAGE_PATH)

df = pd.read_csv(os.path.join(DATA_PATH,'housing.csv'))
from train_test_validation import SplitData
print('Performing stratified train, test, validation split...')
df['income_cat'] =  np.ceil(df['median_income']/1.5)
df['income_cat'].where(df['income_cat']<5,5.0,inplace=True)

sd = SplitData(id_col='income_cat', train_size=0.5, validation_size=0.25, test_size=0.25, random_state=0, mode='stratified')
train_df,validation_df,test_df = sd.fit_transform(df)

test_df.drop('income_cat',axis=1,inplace = True)
train_df.drop('income_cat',axis=1,inplace = True)
validation_df.drop('income_cat',axis=1,inplace = True)

def create_new_cols(df):
    df['rooms_per_household'] = df['total_rooms']/df['households']
    df['bedrooms_per_room'] = df['total_bedrooms']/df['total_rooms']
    df['population_per_household'] = df['population']/df['households']
    return df

train_df = create_new_cols(train_df)
test_df = create_new_cols(test_df)
validation_df = create_new_cols(validation_df)

train_df.to_csv(os.path.join(INTERIM_PATH,'train_df.csv'))
test_df.to_csv(os.path.join(INTERIM_PATH,'test_df.csv'))
validation_df.to_csv(os.path.join(INTERIM_PATH,'validation_df.csv'))
print('Splitting completed')