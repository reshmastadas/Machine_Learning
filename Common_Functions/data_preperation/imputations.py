import pandas as pd
from sklearn.impute import SimpleImputer 
from sklearn.base import BaseEstimator, TransformerMixin

class NullImputation(BaseEstimator, TransformerMixin):
	def __init__(self, parameters,const_val=None):
		'''
			Purpose:
				Imputes all null columns
			Parameters:
				parameters: dictionary with impute strategies
						parameters = {
						'imputation_strategy': [str('median')] # use str() if the list has only one value.
						}
						Possible values for imputations strategy are : mean,median,most_frequent,constant
				const_val: if the imputation strategy is constant, then mention constant value 
			Returns: df,final_imputes
			Author: Reshma Tadas    
		'''
		self.parameters = parameters
		self.const_val = const_val
	def fit(self, X, y=None):
		return self
	def transform(self, X, y=None):
		'''
			Purpose:
				Imputes all null columns
			Parameters:
				X: dataframe 
			Returns: df,final_imputes
			Author: Reshma Tadas    
		'''
		imputation_strategy = self.parameters['imputation_strategy']
		df_new = X.copy()
		X = X._get_numeric_data()
		null_matrix = pd.DataFrame(X.isnull().sum()).reset_index()
		null_cols = list(null_matrix[null_matrix[0]>0]['index'])
		if len(null_cols)!=len(imputation_strategy):
			print('Expecting ',len(null_cols),' imputation strategies, got ',len(imputation_strategy))
			print("Use str() if the list has only one value. Eg: [str('median')]")
			return
		imputer = SimpleImputer(strategy='mean')
		imputer = imputer.fit(X)
		mean_values = imputer.statistics_
		imputer = SimpleImputer(strategy='median')
		imputer = imputer.fit(X)
		median_values = imputer.statistics_
		imputer = SimpleImputer(strategy='most_frequent')
		imputer = imputer.fit(X)
		frequent_values = imputer.statistics_
		final_imputes = []
		for col,col_index in zip(null_cols,range(len(null_cols))):
			if imputation_strategy[col_index]=='mean':
				impute_val = mean_values[col_index]
			elif imputation_strategy[col_index]=='median':
				impute_val = median_values[col_index]
			elif imputation_strategy[col_index]=='most_frequent':
				impute_val = frequent_values[col_index]
			else:
				impute_val = const_val
			final_imputes.append(impute_val)
			df_new[col] = X[col].fillna(impute_val)
		(pd.DataFrame(final_imputes)).to_csv('imputes.csv')
		return df_new
		
class AllImputation(BaseEstimator, TransformerMixin):
	def __init__(self, parameters,const_val=None):
		'''
			Purpose:
				Imputes all columns
			Parameters:
				parameters: dictionary with impute strategies
						parameters = {
						'imputation_strategy': [str('median')] # use str() if the list has only one value.
						}
						Possible values for imputations strategy are : mean,median,most_frequent,constant
				const_val: if the imputation strategy is constant, then mention constant value 
			Returns: df,final_imputes
			Author: Reshma Tadas    
		'''
		self.parameters = parameters
		self.const_val = const_val
	def fit(self,X,y=None):
		return self	
	def transform(self,X,y=None):
		'''
			Purpose:
				Imputes all columns
			Parameters:
				X: dataframe 
			Returns: df,final_imputes
			Author: Reshma Tadas    
		'''
		imputation_strategy = self.parameters['imputation_strategy']
		df_new = X.copy()
		X = X._get_numeric_data()
		null_matrix = pd.DataFrame(X.isnull().sum()).reset_index()
		null_cols = list(null_matrix[null_matrix[0]>0]['index'])
		if len(X.columns)!=len(imputation_strategy):
			print('Expecting ',len(X.columns),' imputation strategies, got ',len(imputation_strategy))
			print("Use str() if the list has only one value. Eg: [str('median')]")
			return
		imputer = SimpleImputer(strategy='mean')
		imputer = imputer.fit(X)
		mean_values = imputer.statistics_
		imputer = SimpleImputer(strategy='median')
		imputer = imputer.fit(X)
		median_values = imputer.statistics_
		imputer = SimpleImputer(strategy='most_frequent')
		imputer = imputer.fit(X)
		frequent_values = imputer.statistics_
		final_imputes = []
		for col,col_index in zip(X.columns,range(len(X.columns))):
			if imputation_strategy[col_index]=='mean':
				impute_val = mean_values[col_index]
			elif imputation_strategy[col_index]=='median':
				impute_val = median_values[col_index]
			elif imputation_strategy[col_index]=='most_frequent':
				impute_val = frequent_values[col_index]
			else:
				impute_val = const_val
			final_imputes.append(impute_val)
			df_new[col] = X[col].fillna(impute_val)
		(pd.DataFrame(final_imputes)).to_csv('imputes.csv')
		return df_new

class CalculateAllImputation(BaseEstimator, TransformerMixin):
	def __init__(self, parameters,const_val=None):
		'''
			Purpose:
				Imputes all columns
			Parameters:
				parameters: dictionary with impute strategies
						parameters = {
						'imputation_strategy': [str('median')] # use str() if the list has only one value.
						}
						Possible values for imputations strategy are : mean,median,most_frequent,constant
				const_val: if the imputation strategy is constant, then mention constant value 
			Returns: df,final_imputes
			Author: Reshma Tadas    
		'''
		self.parameters = parameters
		self.const_val = const_val
	def fit(self,X,y=None):
		return self	
	def transform(self,X,y=None):
		'''
			Purpose:
				Imputes all columns
			Parameters:
				X: dataframe 
			Returns: df,final_imputes
			Author: Reshma Tadas    
		'''
		imputation_strategy = self.parameters['imputation_strategy']
		df_new = X.copy()
		X = X._get_numeric_data()
		null_matrix = pd.DataFrame(X.isnull().sum()).reset_index()
		null_cols = list(null_matrix[null_matrix[0]>0]['index'])
		if len(X.columns)!=len(imputation_strategy):
			print('Expecting ',len(X.columns),' imputation strategies, got ',len(imputation_strategy))
			print("Use str() if the list has only one value. Eg: [str('median')]")
			return
		imputer = SimpleImputer(strategy='mean')
		imputer = imputer.fit(X)
		mean_values = imputer.statistics_
		imputer = SimpleImputer(strategy='median')
		imputer = imputer.fit(X)
		median_values = imputer.statistics_
		imputer = SimpleImputer(strategy='most_frequent')
		imputer = imputer.fit(X)
		frequent_values = imputer.statistics_
		final_imputes = []
		for col,col_index in zip(X.columns,range(len(X.columns))):
			if imputation_strategy[col_index]=='mean':
				impute_val = mean_values[col_index]
			elif imputation_strategy[col_index]=='median':
				impute_val = median_values[col_index]
			elif imputation_strategy[col_index]=='most_frequent':
				impute_val = frequent_values[col_index]
			else:
				impute_val = const_val
			final_imputes.append(impute_val)
		(pd.DataFrame(final_imputes)).to_csv('imputes.csv')
		return final_imputes