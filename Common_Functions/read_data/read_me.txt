/***************************General self defined functions info*****************************/
1. fetch_data_from_url_tgz(data_url, data_path, tgz_name)
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
			
----------------------------------------------------------------------------------------------

2. load_data(path)
		Purpose: 
			read data from excel or csv
        Parameters:
            path: absolute path of file to read
            eg: D:\\hands_on_ml\\book tt.xlsx
        returns:
            dataframe
        imports:
            import pandas as pd
			
----------------------------------------------------------------------------------------------

3. train_test_validation_split(data, train_size=0.5, validation_size=0.25, test_size=0.25,random_state=0):
		Purpose:
			divides data into train_data,validation_data,test_data 
        Parameters: 
            1. data - dataframe
            2. train_size - size of train data 0.5 (50%) default
            3. validation_size - size of validation data 0.25 (25%) default
            4. test_data - size of test data 0.25 (25%) default
            5. random state - seed value for random function
        Imports:
            import pandas as pd
            from sklearn.model_selection import train_test_split
			
----------------------------------------------------------------------------------------------

