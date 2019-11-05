# import data
import os
import sys
import pandas as pd
import numpy as np
from sklearn import preprocessing
from imblearn.over_sampling import SMOTE

# create data paths
RAW_DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','raw'))
INTERIM_DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','interim'))

rsample = SMOTE(sampling_strategy=0.5)

def process_data(df,kind='train'):
    # Droppin ID and Gender
    df = df.drop(['ID','Gender','Unnamed: 0','flag'],axis = 1)
    
    # Label encoding for Agency type, distribution channel
    label_encoder = preprocessing.LabelEncoder()
    df['Agency Type'] = label_encoder.fit_transform(df['Agency Type']) 
    df['Distribution Channel'] = label_encoder.fit_transform(df['Distribution Channel']) 
    
    
    # replacing negative duration by median
    if kind=='train':
        df["Duration"] = np.where(df["Duration"] < 0, df.Duration.median(), df['Duration'])
        imputations =  {
            'column' : ['Duration'],
            'values' : [df.Duration.median()]
        }
        imputations = pd.DataFrame(imputations)
        imputations.to_csv(os.path.join(INTERIM_DATA_PATH,'imputations.csv'))
    else:
        imputations = pd.read_csv(os.path.join(INTERIM_DATA_PATH,'imputations.csv'))
        imputation = imputations[imputations['column']=='Duration']['values'][0]
        df["Duration"] = np.where(df["Duration"] < 0, imputation, df['Duration'])
    
    
    
    # scale values
    scaled_features = preprocessing.StandardScaler().fit_transform(df[['Net Sales','Commision (in value)','Age']])
    scaled_features = pd.DataFrame(scaled_features, index=df.index, columns=['Net Sales','Commision (in value)','Age'])
    df['Net Sales'] = scaled_features['Net Sales']
    df['Commision (in value)'] = scaled_features['Commision (in value)']
    df['Age'] = scaled_features['Age']
    
    
    if kind=='train':
        X = df.drop('Claim',axis=1)
        y = df['Claim']

        X_res, y_res = rsample.fit_resample(X,y)
        X_res = pd.DataFrame(X_res, columns = X.columns)
        y_res = pd.DataFrame(y_res, columns = ['Claim'])
        X_res['Claim'] = y_res['Claim']
        df = X_res
    
    return df

def calculate_dummies(df_train,df_test,df_val):
    df_train['flag']=1
    df_test['flag']=0
    df_val['flag']=2
    combined = pd.concat([df_train,df_test,df_val])
    combined = pd.get_dummies(data=combined, columns=['Product Name', 'Destination','Agency'])
    df_train=combined[combined['flag']==1]
    df_test = combined[combined['flag']==0]
    df_val = combined[combined['flag']==2]
    return df_train,df_test,df_val

df_train = pd.read_csv(os.path.join(RAW_DATA_PATH,'train_set.csv'))

df_test = pd.read_csv(os.path.join(RAW_DATA_PATH,'test_set.csv'))

df_val = pd.read_csv(os.path.join(RAW_DATA_PATH,'val_set.csv'))

df_train, df_test, df_val = calculate_dummies(df_train,df_test,df_val)

df_train = process_data(df_train,'train')

df_test = process_data(df_test,'test')

df_val = process_data(df_val,'test')
df_test.to_csv(os.path.join(INTERIM_DATA_PATH,'test_set.csv'))
df_train.to_csv(os.path.join(INTERIM_DATA_PATH,'train_set.csv'))
df_val.to_csv(os.path.join(INTERIM_DATA_PATH,'val_set.csv')) 