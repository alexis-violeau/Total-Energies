import pandas as pd
import numpy as np
from pyproj import Proj, transform

COLS = ['objetID', 'longueur', 'xD', 'yD', 'xF', 'yF','typeComptageTrafic', 'TMJA', 'ratio_PL' ]

def only_Vosges(df, dep=88):
    return df[ (df.depPrD == dep) | (df.depPrF == dep) ]

def keep_useful_cols(df, cols=COLS):
    return df[cols]

def transform_coordinates(df):
    inProj = Proj(init='epsg:2154')
    outProj = Proj(init='epsg:4326')
    xD = np.array(df.xD)
    yD = np.array(df.yD)
    xF = np.array(df.xF)
    yF = np.array(df.yF)

    longD, latD = transform(inProj,outProj,xD, yD)
    longF, latF = transform(inProj,outProj,xF, yF)

    df['longD'] = longD.tolist()
    df['latD'] = latD.tolist()
    df['longF'] = longF.tolist()
    df['latF'] = latF.tolist()

    df = df.drop(['xD', 'yD', 'xF', 'yF'], axis=1)
    return df