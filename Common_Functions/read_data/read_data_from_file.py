import pandas as pd

def load_data(path):
    '''
        Purpose: read data from excel or csv
        Parameters:
            path: absolute path of file to read
            eg: D:\\hands_on_ml\\book tt.xlsx
        returns:
            dataframe
        imports:
            import pandas as pd
        Author:
            Reshma Tadas
    '''
    ext = path.split('.')[-1]
    if ext == 'csv':
        return pd.read_csv(path)
    elif ext == 'xlsx':
        return pd.read_excel(path)