import pandas as pd
from tqdm import tqdm
import sys
sys.path.append("../")

YEAR_RANGE = range(2012,2022)

def load_vehicule_data(path = '../data/vp_communes.csv'):
    """Load existing data on historical automobile parc in France at the communal level

    Args:
        path (str, optional): path to download data. Defaults to 'data/parc_vp_communes'.
        
    Return:
        pandas.DataFrame : All historical data at the department level
    """ 
    return pd.read_csv(path).drop(columns=['Unnamed: 0'])

def load_demographic_data(path = 'Data/demographic.xlsx'):
    """Load demographic data (both historical and projection) of french population at the department level.
    Args:
        path (str, optional): Path to data_. Defaults to 'Data/'.
    """
    
    df = pd.DataFrame()
    
    for year in tqdm(YEAR_RANGE):
        df_year = pd.read_excel(path,sheet_name = str(year), index_col = [0,1], header = [0,1])
        df_year['year'] = year
        df = pd.concat([df,df_year])
    
    return df