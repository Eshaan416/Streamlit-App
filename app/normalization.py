import pandas as pd
import streamlit as st

@st.cache_data
def normalized_dataframes(df_json):
    list=['categoryType','productUrl','catlevel2Name','sku','catlevel3Name','catlevel1Name','catlevel4Name','name','size']
    for col in df_json.columns:
        if col in list:
            del df_json[col]
    df_categories=pd.DataFrame(columns=['uniqueId','level','cat'])
    for index,row in df_json.iterrows():
        levels=1
        for category in row['category']:
           df_categories.loc[len(df_categories.index)] = [row['uniqueId'],levels,category]
           levels=levels+1
    del df_json['category']
    return df_json,df_categories
