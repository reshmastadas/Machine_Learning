# -*- coding: utf-8 -*-
import os 
import sys
from six.moves import urllib
from zipfile import ZipFile 
from sklearn.base import BaseEstimator, TransformerMixin

DOWNLOAD_URL = 'https://www.kaggle.com/c/12500/download-all'
DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','raw'))
PACKAGE_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,os.path.pardir,
                                            'Common_Functions','read_data'))
sys.path.insert(1, PACKAGE_PATH)
from fetch_data_from_url import DownloadDataFromURL
fetch_data = DownloadDataFromURL(DOWNLOAD_URL,DATA_PATH,'jigsaw-unintended-bias-in-toxicity-classification.zip')
fetch_data.fit_transform(X=None,y=None)
with ZipFile(os.path.join(DATA_PATH,'jigsaw-unintended-bias-in-toxicity-classification.zip'), 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall(DATA_PATH) 
    print('Done!') 

