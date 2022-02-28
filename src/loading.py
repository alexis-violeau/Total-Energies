import pandas as pd
import sys
sys.path.append("../")

def load_vehicule_data(path = '../data/vp_communes.csv'):
    """Load existing data on historical automobile parc in France at the communal level

    Args:
        path (str, optional): path to download data. Defaults to 'data/parc_vp_communes'.
        
    Return:
        pandas.DataFrame : All historical data at the department level
    """ 
    return pd.read_csv(path).drop(columns=['Unnamed: 0'])

def load_demographic_data(path = 'Data/'):
    """Load demographic data (both historical and projection) of french population at the department level.

    Args:
        path (str, optional): Path to data_. Defaults to 'Data/'.
    """
    
    # TODO
    
    return

