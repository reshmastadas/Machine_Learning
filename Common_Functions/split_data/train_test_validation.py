import pandas as pd
import hashlib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.base import BaseEstimator, TransformerMixin

class SplitData(BaseEstimator,TransformerMixin):
	def __init__(self, id_col='0', train_size=0.5, validation_size=0.25, test_size=0.25,random_state=0,mode='normal'):
		self.id_col = id_col
		self.train_size = train_size
		self.validation_size = validation_size
		self.test_size = test_size
		self.random_state = random_state
		self.mode = mode
		'''
			Purpose: 
				Divide data into train, validation and test dataframes.
			Parameters:
				data: name of dataframe
				id_col: when mode is id, this is column with primary keys
						when mode is stratified, this is the categorical column to stratify
				train_size: size of train data
				test_size: size of test data
				validation_data: size of validation data
				mode: normal: direct train, test, validation split (used when no primery key column is available)
					  id: divides data based on id_column (prferred)
					  stratified: divides data by considering ratio in a categorical column (preferred when there is an important categorical feature)
			Imports:
				import pandas as pd
				import hashlib
				import numpy as np
				from sklearn.model_selection import train_test_split
				from sklearn.model_selection import StratifiedShuffleSplit
				from sklearn.base import BaseEstimator, TransformerMixin
		'''
	
	def fit(self,X,y=None):
		return self
	
	def transform(self,X,y=None):
		'''
			Purpose:
				Divide data into train, validation and test dataframes.
			Parameters:
				X: dataframe to divide
			Returns:
				train,validation and test data
			Author: 
				Reshma Tadas
		'''
		if self.mode=='normal':
			nrows = X.shape[0]
			trnr = int(nrows*self.train_size)
			vlnr = int(nrows*self.validation_size)
			train_data, remaining = train_test_split(X, train_size=trnr,random_state=self.random_state)
			validation_data, test_data = train_test_split(remaining, train_size = vlnr, random_state=self.random_state)
			return (train_data,validation_data,test_data)
		if self.mode=='id':
			def test_set_check(identifier, test_ratio,validation_ratio,hash):
				if hash(np.int64(identifier)).digest()[-1]<256*test_ratio:
					return 2
				if hash(np.int64(identifier)).digest()[-1]<256*(test_ratio+validation_ratio) and  hash(np.int64(identifier)).digest()[-1]>256*test_ratio:
					return 1
				return 0
			hash = hashlib.md5
			ids = X[self.id_col]
			in_test_set = ids.apply(lambda id_: test_set_check(id_,self.test_size,self.validation_size,hash)==2)
			in_validation_set = ids.apply(lambda id_: test_set_check(id_,self.test_size,self.validation_size,hash)==1)
			in_train_set = ids.apply(lambda id_: test_set_check(id_,self.test_size,self.validation_size,hash)==0)
			return X.loc[in_train_set],X.loc[in_validation_set],X.loc[in_test_set]
		if self.mode=='stratified':
			split = StratifiedShuffleSplit(n_splits=1,test_size=self.test_size,random_state=self.random_state)
			for train_index, test_index in split.split(X,X[self.id_col]):
				train_set = X.iloc[train_index]
				test_set = X.iloc[test_index]
			modified_validation_ratio = (X.shape[0]*self.validation_size)/train_set.shape[0]
			split_1 = StratifiedShuffleSplit(n_splits=1,test_size=modified_validation_ratio,random_state=self.random_state)
			for train_index, test_index in split_1.split(train_set,train_set[self.id_col]):
				train_df = train_set.iloc[train_index]
				validation_set = train_set.iloc[test_index]
			return train_df,validation_set,test_set