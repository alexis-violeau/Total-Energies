import pandas as pd
import os

def build_vp_communes(path):
    vp_communes = pd.DataFrame()
    for year in range(2012, 2022):
        print("Inserting data for year",year)
        df = pd.read_excel(os.path.join(path, f"Parc_VP_Communes_{year}.xlsx"))
        df.drop(columns=["Code Epci","Libellé EPCI","Code commune","Libellé commune"], inplace=True)
        df.rename(columns={f"Parc au 01/01/{year}":"parc"}, inplace=True)
        df["annee"] = year
        vp_communes = pd.concat([vp_communes, df])
    vp_communes.rename(columns={"Code région":"c_region", 
                                   "Libellé région":"l_region", 
                                   "Code départment":"c_dep",
                                   "Libellé département":"l_dep", 
                                   "Vignette Crit'air":"crit_air", 
                                   "Energie":"energie"}, inplace=True)
    vp_dep = vp_communes.groupby(by=['c_region', 'l_region', 'c_dep', 'l_dep', 'crit_air', 'energie','annee']).sum()
    vp_dep.reset_index(inplace=True)
    return vp_dep

def main():
    save_path = "data"
    vp_communes = build_vp_communes("raw_data/Challenge #1/parc_vp_communes")
    vp_communes.to_csv(os.path.join(save_path,"vp_dep.csv"))
    
if __name__=="__main__":
    main()
    