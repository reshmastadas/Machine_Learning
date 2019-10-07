import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from os.path import join, abspath, dirname, pardir

BASE_DIR = abspath(join(dirname(__file__),pardir))
DATA_DIR = join(BASE_DIR, 'data')
DATA_DIR = join(DATA_DIR, 'raw')

def load_all_transactions(filename):
    """
    Loads all transacion data provided in the csv file
    target variable class is included in the dataframe
    """
    transacions = pd.read_csv(join(DATA_DIR, filename))
    print('\nTher are a toral of {} transactions and {} features \n'.format(transacions.shape[0],transacions.columns))
    return transacions

def features_target_split():
    """Splits the data into independent(X) and dependent(Y) variables."""
    transactions = load_all_transactions('creditcard.csv')
    features = transactions.drop('Class', axis=1)
    target = transactions['Class']
    print('\nCreation of feature set dataframe and target seiries successful \n')
    return features, target

def load_train_test_transactions(train_size=0.7):
    """
    Loads all the train transactions data based on threshold balue.
    taget variable class is returned as seperate padnas series"""
    X, y = features_target_split()
    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=train_size, random_state=7)
    print('\nTraining and testing data creation successful\n')
    return X_train, X_test, y_train,y_test

if __name__ == '__main__':
    train_X, test_X, train_y, test_y = load_train_test_transactions()
    print(test_X.head())
