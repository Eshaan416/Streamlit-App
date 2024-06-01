import streamlit as st
import pandas as pd
from sqlalchemy import text
from normalization import normalized_dataframes
from insertion import insert_data

conn = st.connection('postgresql', 'sql')

uploaded_json=st.file_uploader('Drop your database in json format',['json'],False)

if uploaded_json is not None:
    
    df=pd.read_json(uploaded_json)
    
    df_items,df_categories=normalized_dataframes(df)
    
    insert_data(df_items,df_categories)
        
    test=conn.query('select * from items')
    st.write(test)
    test2=conn.query('select * from categories')
    st.write(test2)
    
        
