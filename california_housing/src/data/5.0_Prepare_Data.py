import pandas as pd
import os
import sys
from sklearn.impute import SimpleImputer 
import pandas as pd

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'data','interim'))
PROCESSED_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'data','processed'))
PACKAGE_PATH =  os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,os.path.pardir,
                                            'Common_Functions','data_preperation'))

train_df = pd.read_csv(os.path.join(DATA_PATH,'train_df.csv'))

housing = train_df.drop('median_house_value',axis=1)
housing_labels = train_df['median_house_value']

sys.path.insert(1, PACKAGE_PATH)

from imputations import AllImputation
from Scaling import Scaler

parameters = {
    'imputation_strategy': ['median','median','median','median','median','median','median','median','median','median','median','median'] # use str() if the list has only one value.
}

req_cols=['longitude','latitude','housing_median_age','total_rooms', 'total_bedrooms', 'population', 'households',
       'median_income', 'rooms_per_household', 'bedrooms_per_room',
       'population_per_household']
   
from sklearn.pipeline import Pipeline


steps = Pipeline([
    ('impute', AllImputation(parameters=parameters,const_val=None)),
    ('scale' , Scaler(req_cols=req_cols))
])

def prepare_data(df,parameters,req_cols=req_cols,target=None):
    if target!=None:
        x = df.drop(target,axis=1)
        y = df[target]
        y.columns = [target]
    else:
        x = df
    x = steps.fit_transform(x)
    x = pd.get_dummies(x,prefix=['proximity'],columns=['ocean_proximity'])
    x.drop('Unnamed: 0',axis=1,inplace=True)
    return x,pd.DataFrame(y)
x,y = prepare_data(train_df,parameters=parameters,req_cols=req_cols,target = 'median_house_value')
x.to_csv(os.path.join(PROCESSED_PATH,'x.csv'))
y.to_csv(os.path.join(PROCESSED_PATH,'y.csv'))

validation_df = pd.read_csv(os.path.join(DATA_PATH,'validation_df.csv'))

x_val,y_val= prepare_data(validation_df,parameters=parameters,req_cols=req_cols,target = 'median_house_value')
x_val.to_csv(os.path.join(PROCESSED_PATH,'x_val.csv'))
y_val.to_csv(os.path.join(PROCESSED_PATH,'y_val.csv'))

test_df = pd.read_csv(os.path.join(DATA_PATH,'test_df.csv'))
x_test,y_test= prepare_data(test_df,parameters=parameters,req_cols=req_cols,target = 'median_house_value')
x_test.to_csv(os.path.join(PROCESSED_PATH,'x_test.csv'))
y_test.to_csv(os.path.join(PROCESSED_PATH,'y_test.csv'))