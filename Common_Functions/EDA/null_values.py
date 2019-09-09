import pandas as pd

def find_null_percent(df):
	'''
	Purpose:
		Function to find % of null values in each column of a dataframe.
	Input:
		df: Dataframe.
	Returns:
		null_df: a dataframe with % of null values.
	Imports:
		import pandas as pd
	Author: Reshma Tadas
	'''
	null_df = pd.DataFrame(df.isnull().sum()).reset_index()
	null_df[0] = null_df[0]/len(df)
	null_df[0] = null_df[0].apply(lambda x: str(round(x,4)*100)+' %')
	return null_df
	
def get_num_cat_cols(df,limit=10):
	'''
	Purpose:
		Function to get numerical and categorical columns of a dataframe.
	Input:
		df: Dataframe.
		limit: max number of unique values allowed in categorical column.
	Returns:
		num_cols: numerical columns
		cat_cols: categorical columns
	Imports:
		import pandas as pd
	Author: Reshma Tadas
	'''
	unique_df = pd.DataFrame(df.nunique()).reset_index()
	cat_cols = list(unique_df[unique_df[0]<=limit]['index'])
	num_cols = list(unique_df[unique_df[0]>limit]['index'])
	return (num_cols,cat_cols)