import pandas as pd
from tqdm import tqdm

YEAR_RANGE = range(2012,2022)

def load_vp(path = 'data/parc_vp_communes.csv'):
    """Load existing data on historical automobile fleet in France at the communal level

    Args:
        path (str, optional): Path to data. Defaults to 'data/parc_vp_communes'.
        
    Return:
        pandas.DataFrame : Vehicule historic
    """
    
    return pd.read_csv(path)

def load_demo(path = 'data/demographic.xlsx'):
    """Load demographic data of french population at the department/age/year levels.

    Args:
        path (str, optional): Path to data. Defaults to 'data/demographic.xlsx'.
        
    Return:
        pandas.DataFrame : Demographic historic
    """
    
    df = pd.DataFrame()
    
    for year in tqdm(YEAR_RANGE):
        df_year = pd.read_excel(path,sheet_name = str(year),header = [0,1])
        df_year['year'] = year
        df = pd.concat([df,df_year])
    
    return df

def load_taffic(path='Data/Données trafic routier open data TMJA2019.xlsx'):
    """Load existing data on the average traffic per day

    Args:
        path (str, optional): Path to data. Defaults to 'data/parc_vp_communes'.
        
    Return:
        pandas.DataFrame : Taffic historic
    """
    return pd.read_excel(path)

