1. null_imputation
	Purpose:
        Imputes all null columns
    Parameters:
        df: dataframe
        parameters: dictionary with impute strategies
                parameters = {
                'imputation_strategy': [str('median')] # use str() if the list has only one value.
                }
                Possible values for imputations strategy are : mean,median,most_frequent,constant
        const_val: if the imputation strategy is constant, then mention constant value 
    Returns: df,final_imputes
	
2. all_imputation
	Purpose:
        Imputes all columns
    Parameters:
        df: dataframe
        parameters: dictionary with impute strategies
                parameters = {
                'imputation_strategy': [str('median')] # use str() if the list has only one value.
                }
                Possible values for imputations strategy are : mean,median,most_frequent,constant
        const_val: if the imputation strategy is constant, then mention constant value 
    Returns: df,final_imputes
	
3. calculate_all_imputation
	Purpose:
        Imputes all columns
    Parameters:
        df: dataframe
        parameters: dictionary with impute strategies
                parameters = {
                'imputation_strategy': [str('median')] # use str() if the list has only one value.
                }
                Possible values for imputations strategy are : mean,median,most_frequent,constant
        const_val: if the imputation strategy is constant, then mention constant value 
    Returns: final_imputes