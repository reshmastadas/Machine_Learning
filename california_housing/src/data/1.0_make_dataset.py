import os 
import sys
import tarfile
from six.moves import urllib
from sklearn.base import BaseEstimator, TransformerMixin

print('Reading data and storing in raw folder...')
PACKAGE_PATH =  os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,os.path.pardir,
                                            'Common_Functions','read_data'))
DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
HOUSEING_PATH = 'datasets/housing'
HOUSING_URL = DOWNLOAD_ROOT + HOUSEING_PATH + '/housing.tgz'
HOUSEING_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','raw'))

sys.path.insert(1, PACKAGE_PATH)
from fetch_data_from_url import FetchDataFromURLTGZ
fetch_data = FetchDataFromURLTGZ(HOUSING_URL,HOUSEING_PATH,'/housing.tgz')
fetch_data.fit_transform(X=None,y=None)
print('Data reading is done')