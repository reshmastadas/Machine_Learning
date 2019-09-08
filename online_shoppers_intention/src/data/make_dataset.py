# -*- coding: utf-8 -*-
import os 
import sys
from six.moves import urllib
from zipfile import ZipFile 
from sklearn.base import BaseEstimator, TransformerMixin

DOWNLOAD_URL = 'https://storage.googleapis.com/kaggle-datasets/201937/444614/online-shoppers-intention.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1567752166&Signature=KE7sO2ysQQNei5DLNLYSBAO68qk7pHGr%2FlI0XT54Ig8LLizZlFta8bhwTKU%2FAdz6EgkPhMiEk7E48EHV%2FQdiKEGL9aHtNtstL%2Fv4c2kiHW74xFHJcMKXBd5waG1nrHF1Ugvmgxwwk0ENbHdcD%2FlSBYqHWqkAXcD4bOLNdEwKMWqZYgAzbIC6jtICaK6oOPxqAFw2nwWd0210Tk%2FrhRbKYXbiLsiYGEBNp%2FMt3I74K2Axx7o9UjhFQGsF7awi8iNWMAwogxbNqH6LFQQsMZt51oC43HxQyCsQu6H0NKEA08mDyGgFokeQ3kSIIcWMXzYrW%2BmtHJpyhusC9AD8crVXQg%3D%3D'
DATA_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,'data','raw'))
PACKAGE_PATH = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir,os.path.pardir,os.path.pardir,
                                            'Common_Functions','read_data'))
sys.path.insert(1, PACKAGE_PATH)
from fetch_data_from_url import DownloadDataFromURL
fetch_data = DownloadDataFromURL(DOWNLOAD_URL,DATA_PATH,'online_shoppers_intention.zip')
fetch_data.fit_transform(X=None,y=None)
with ZipFile(os.path.join(DATA_PATH,'online_shoppers_intention.zip'), 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall(DATA_PATH) 
    print('Done!') 

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
