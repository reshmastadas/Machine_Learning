from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import os


DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'data','processed'))
RESULT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'data','final'))


x=pd.DataFrame(pd.read_csv(os.path.join(DATA_PATH,'x.csv'))).drop('Unnamed: 0',axis=1)
y=pd.read_csv(os.path.join(DATA_PATH,'y.csv')).drop('Unnamed: 0',axis=1)
x_val=pd.read_csv(os.path.join(DATA_PATH,'x_val.csv')).drop('Unnamed: 0',axis=1)
y_val=pd.read_csv(os.path.join(DATA_PATH,'y_val.csv')).drop('Unnamed: 0',axis=1)
x_test=pd.read_csv(os.path.join(DATA_PATH,'x_test.csv')).drop('Unnamed: 0',axis=1)
y_test=pd.read_csv(os.path.join(DATA_PATH,'y_test.csv')).drop('Unnamed: 0',axis=1)

param_grid = [
    {'n_estimators': [3,10,30], 'max_features': [2,3,4]},
    {'bootstrap': [False], 'n_estimators': [3,10], 'max_features': [2,3,4]}
]

forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring = 'neg_mean_squared_error')
grid_search.fit(x,y)

print("The final model gives following score while doing cross validation:\n")

cvres = grid_search.cv_results_
for mean_score, params in zip(cvres['mean_test_score'], cvres['params']):
    print(np.sqrt(-mean_score),params)

	
print('-'*40)
print("Mean squared error on validation set:\n")
y_pred = grid_search.predict(x_val)
print(np.sqrt(mean_squared_error(y_pred,y_val)))


print('-'*40)
print("Mean squared error on test set:\n")
y_pred = grid_search.predict(x_test)
print(np.sqrt(mean_squared_error(y_pred,y_test)))
y_pred = pd.DataFrame(y_pred)
y_pred.to_csv(os.path.join(RESULT_PATH,'predictions.csv'))