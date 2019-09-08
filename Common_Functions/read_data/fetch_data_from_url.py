import os 
import tarfile
from six.moves import urllib
from sklearn.base import BaseEstimator, TransformerMixin

class FetchDataFromURLTGZ(BaseEstimator, TransformerMixin):
	def __init__(self, data_url, data_path, tgz_name):
		'''
			Purpose:
				Downloads tgz from url and extracts the same in mentioned path.
			Parameters: 
				data_url: url for tgz file.
						  eg: https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz
				data_path: path in hardrive to save data.
						  eg: datasets - HAS TO BE SINGLE LEVEL
				tgz_name: name of tgz file.
						  eg: housing.tgz
			Imports:
				import os 
				import tarfile
				from six.moves import urllib
				from sklearn.base import BaseEstimator, TransformerMixin
			Author:
				Reshma Tadas
		'''
		self.data_url = data_url
		self.data_path = data_path
		self.tgz_name = tgz_name
	def fit(self,X=None,y=None):
		return self
	def transform(self,X=None,y=None):
		'''
			Purpose:
				Downloads tgz from url and extracts the same in mentioned path.
			Imports:
				import os 
				import tarfile
				from six.moves import urllib
			Author:
				Reshma Tadas
		'''
		if not os.path.isdir(self.data_path):
			os.mkdir(self.data_path)
		tgz_path = os.path.join(self.data_path,self.tgz_name)
		urllib.request.urlretrieve(self.data_url,tgz_path)
		data_tgz = tarfile.open(tgz_path)
		data_tgz.extractall(path=self.data_path)
		data_tgz.close()

class DownloadDataFromURL(BaseEstimator, TransformerMixin):
	def __init__(self, data_url, data_path, tgz_name):
		'''
			Purpose:
				Downloads from in mentioned path.
			Parameters: 
				data_url: url for tgz/zip file.
						  eg: https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz
				data_path: path in hardrive to save data.
						  eg: datasets - HAS TO BE SINGLE LEVEL
				tgz_name: name of tgz file.
						  eg: housing.tgz
			Imports:
				import os 
				from six.moves import urllib
				from sklearn.base import BaseEstimator, TransformerMixin
			Author:
				Reshma Tadas
		'''
		self.data_url = data_url
		self.data_path = data_path
		self.tgz_name = tgz_name
	def fit(self,X=None,y=None):
		return self
	def transform(self,X=None,y=None):
		'''
			Purpose:
				Downloads tgz from url and extracts the same in mentioned path.
			Imports:
				import os 
				import tarfile
				from six.moves import urllib
			Author:
				Reshma Tadas
		'''
		if not os.path.isdir(self.data_path):
			os.mkdir(self.data_path)
		tgz_path = os.path.join(self.data_path,self.tgz_name)
		urllib.request.urlretrieve(self.data_url,tgz_path)