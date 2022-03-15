import pandas as pd
import numpy as np
import os

YEAR_RANGE = range(2012, 2022)

def build_vp_communes(path = 'data/parc_vp_communes'):
    """Building aggregate VP data at the department level for each year

    Args:
        path (str, optional): Path to data. Defaults to 'data/parc_vp_communes'.

    Returns:
        pandas.DataFrame: Aggregated data at the department level for each year
    """
    
    vp_communes = pd.DataFrame()
    
    # We iterate over the year in the year range of our data
    for year in YEAR_RANGE:
        print("Inserting data for year",year)
        df = pd.read_excel(os.path.join(path, f"Parc_VP_Communes_{year}.xlsx"))
        
        # We drop some useless columns and rename others
        df.drop(columns=["Code Epci","Libellé EPCI","Code commune","Libellé commune"], inplace=True)
        df.rename(columns={f"Parc au 01/01/{year}":"parc"}, inplace=True)
        
        # We keep the year information and concatenate with data of previous years
        df["annee"] = year
        vp_communes = pd.concat([vp_communes, df])
        
    vp_communes.rename(columns={"Code région":"c_region", 
                                   "Libellé région":"l_region", 
                                   "Code départment":"c_dep",
                                   "Libellé département":"l_dep", 
                                   "Vignette Crit'air":"crit_air", 
                                   "Energie":"energie"}, inplace=True)
    
    
    # We aggregate the data at the departement level for each type of vehicule
    vp_dep = vp_communes.groupby(by=['c_region', 'l_region', 'c_dep', 'l_dep', 'crit_air', 'energie','annee']).sum()
    vp_dep.reset_index(inplace=True)
    
    # Manage missing values
    vp_dep = vp_dep.replace({'Inconnu':np.nan,'Inconnue':np.nan,'XX':np.nan,'Non classée':np.nan})
    
    # Order crit_air 
    vp_communes['crit_air'] = vp_communes['crit_air'].replace({"Crit'air E":0,
                                                               "Crit'air 1":1,
                                                               "Crit'air 2":2,
                                                               "Crit'air 3":3,
                                                               "Crit'air 4":4,
                                                               "Crit'air 5":5}).astype(float)
    
    return vp_communes


def build_demographic(path = 'data/'):
    df_demo = pd.DataFrame()
        
    for year in YEAR_RANGE:
        df_year = pd.read_excel(path + 'demographic.xlsx',sheet_name = str(year),header = [0,1])
        df_year['year'] = year
        df_demo = pd.concat([df_demo,df_year])
        
    df_surf = pd.read_excel(path + 'Surfaces.xlsx', header = [0,1])

    df_merge = df_demo.merge(df_surf, left_on = [('Départements','Numéro')], right_on = [('Départements','Numéro')])

    df_merge['Actifs'] = df_merge['Ensemble']['20 à 39 ans'] + df_merge['Ensemble']['40 à 59 ans'] + df_merge['Ensemble']['60 à 74 ans']
    df_merge['Densite'] = df_merge['Ensemble']['Total'] / df_merge['Surface']['km2']
    df_merge['c_dep'] = df_merge['Départements']['Numéro']
    df_merge['annee'] = df_merge['year'].astype(int)

    return df_merge[['c_dep','Actifs','Densite','annee']].set_index(['c_dep','annee']).droplevel(level = 1,axis = 1)

        


def main():
    save_path = "data"
    vp_communes = build_vp_communes('data/parc_vp_communes')
    vp_communes.to_csv(os.path.join(save_path,"parc_vp_communes.csv"),index = False)
    df_demographic = build_demographic('data/')
    df_demographic.to_csv(os.path.join(save_path,"demographic_condensed.csv"),index = False)
    
if __name__=="__main__":
    main()
    