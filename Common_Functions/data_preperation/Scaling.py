import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator, TransformerMixin

class Scaler(BaseEstimator, TransformerMixin):
	def __init__(self, req_cols, method='standard'):
		'''
			Purpose: Scaling dataframe
			Parameters:
				req_cols: list of required columns
				method: either standard or minmax
			Imports:
				import pandas as pd
				from sklearn.preprocessing import StandardScaler
				from sklearn.preprocessing import MinMaxScaler
				from sklearn.base import BaseEstimator, TransformerMixin
			Author: 
				Reshma Tadas
		'''
		self.req_cols = req_cols
		self.method = method
	def fit(self, X, y=None):
		return self
	def transform(self, X, y=None):
		'''
			Purpose: Scaling dataframe
			Parameters:
				X: dataframe to scale
			Author: 
				Reshma Tadas
		'''
		X = pd.DataFrame(X)
		df_new=X[self.req_cols]
		if self.method == 'standard':
			std = StandardScaler()
			df = pd.DataFrame(std.fit_transform(df_new))
		else:
			minmax = MinMaxScaler()
			df = pd.DataFrame(minmax.fit_transform(df_new))
		for col,col_index in zip(self.req_cols,range(len(self.req_cols))):
			X[col]=df[col_index]
		return X