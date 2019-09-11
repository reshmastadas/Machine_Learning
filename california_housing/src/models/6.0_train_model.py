from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import os
import sys

DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','processed'))
PACKAGE_PATH = os.path.join(os.getcwd(),os.path.pardir,'Common_Functions','data_preperation')
sys.path.insert(1, PACKAGE_PATH)

x=pd.DataFrame(pd.read_csv(os.path.join(DATA_PATH,'x.csv'))).drop('Unnamed: 0',axis=1)
y=pd.read_csv(os.path.join(DATA_PATH,'y.csv')).drop('Unnamed: 0',axis=1)
x_val=pd.read_csv(os.path.join(DATA_PATH,'x_val.csv')).drop('Unnamed: 0',axis=1)
y_val=pd.read_csv(os.path.join(DATA_PATH,'y_val.csv')).drop('Unnamed: 0',axis=1)
x_test=pd.read_csv(os.path.join(DATA_PATH,'x_test.csv')).drop('Unnamed: 0',axis=1)
y_test=pd.read_csv(os.path.join(DATA_PATH,'y_test.csv')).drop('Unnamed: 0',axis=1)

def fit_model(model,x,y,x_val,y_val,model_name):
    model=model.fit(x,y)
    y_pred = model.predict(x)
    rmse = mean_squared_error(y,y_pred)
    rmse = np.sqrt(rmse)
    print('\nRMSE of',model_name,'with training set is:\t',rmse)
    y_pred = model.predict(x_val)
    rmse = mean_squared_error(y_val,y_pred)
    rmse = np.sqrt(rmse)
    print('RMSE of',model_name,'with validation set is:\t',rmse)

lr = LinearRegression()
dtree = DecisionTreeRegressor()
freg = RandomForestRegressor()
svm = SVR() # default=rbf
svm_linear = SVR(kernel='linear')
svm_poly = SVR(kernel='poly')

fit_model(lr,x,y,x_val,y_val,model_name='Linear Regressor')
fit_model(dtree,x,y,x_val,y_val,model_name='Decision Tree Regressor')
fit_model(freg,x,y,x_val,y_val,model_name='Random Forest Regressor')
fit_model(svm,x,y,x_val,y_val,model_name='SVM_rbf')
fit_model(svm_linear,x,y,x_val,y_val,model_name='SVM_linear')
fit_model(svm_poly,x,y,x_val,y_val,model_name='SVM_poly')

from sklearn.model_selection import cross_val_score
scores = cross_val_score(dtree,x,y,scoring='neg_mean_squared_error',cv=10)
tree_rmse_scores = np.sqrt(-scores)
def display_scores(scores):
    print('scores:\n',scores)
    print('Mean Scores:\n',scores.mean())
    print('Standard Deviation:\n',scores.std())
display_scores(tree_rmse_scores)
scores = cross_val_score(lr,x,y,scoring='neg_mean_squared_error',cv=10)
lr_rmse_scores = np.sqrt(-scores)
display_scores(lr_rmse_scores)
scores = cross_val_score(freg,x,y,scoring='neg_mean_squared_error',cv=10)
freg_rmse_scores = np.sqrt(-scores)
display_scores(freg_rmse_scores)
scores = cross_val_score(svm,x,y,scoring='neg_mean_squared_error',cv=10)
svm_rmse_scores = np.sqrt(-scores)
display_scores(svm_rmse_scores)
scores = cross_val_score(svm_linear,x,y,scoring='neg_mean_squared_error',cv=10)
svm_linear_rmse_scores = np.sqrt(-scores)
display_scores(svm_linear_rmse_scores)
scores = cross_val_score(svm_poly,x,y,scoring='neg_mean_squared_error',cv=10)
svm_poly_rmse_scores = np.sqrt(-scores)
display_scores(svm_poly_rmse_scores)

from sklearn.externals import joblib
def save_model(model,hpyer_params,cross_val_scores,model_name='model_name',path=os.getcwd()):
    data_path = os.path.join(path,model_name)
    if not os.path.isdir(data_path):
        os.mkdir(data_path)
    joblib.dump(model,os.path.join(data_path,model_name+'.pkl'))
    hpyer_params=pd.DataFrame(hpyer_params)
    hpyer_params.to_csv(os.path.join(data_path,'hyper_params.csv'))
    cross_val_scores=pd.DataFrame(cross_val_scores)
    cross_val_scores.to_csv(os.path.join(data_path,'cross_val_scores.csv'))
hyper_params = {'params':[]}
save_model(lr,hyper_params,lr_rmse_scores,'Linear_Regression',DATA_PATH)
save_model(dtree,hyper_params,tree_rmse_scores,'Decsion_Tree',DATA_PATH)
save_model(freg,hyper_params,freg_rmse_scores,'Random_Forest',DATA_PATH)
hyper_params = {'kernel':[str('rbf')]}
save_model(svm,hyper_params,svm_rmse_scores,'SVM_RBF',DATA_PATH)
hyper_params = {'kernel':[str('linear')]}
save_model(svm_linear,hyper_params,svm_linear_rmse_scores,'SVM_Linear',DATA_PATH)
hyper_params = {'kernel':[str('poly')]}
save_model(svm_poly,hyper_params,svm_poly_rmse_scores,'SVM_Poly',DATA_PATH)