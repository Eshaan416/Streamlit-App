import streamlit as st
import pandas as pd
st.write(st.secrets)
from sqlalchemy import text
from normalization import normalized_dataframes
from insertion import insert_data
from queries import cat_level, get_by_name, get_by_uniqueid

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

import streamlit as st
import pandas as pd

# Title of the app
st.title("Input Form")

# Drop-down menu for input selection
input_choice = st.selectbox("Choose input type", ["Name", "UniqueID", "Category"])

# Display input field based on selection
if input_choice == "Name":
    name = st.text_input("Name")
    unique_id = ""
    category = ""
    category_level = None
elif input_choice == "UniqueID":
    unique_id = st.text_input("UniqueID")
    name = ""
    category = ""
    category_level = None
elif input_choice == "Category":
    category = st.text_input("Category")
    category_level = st.text_input("Category Level", "This field is mandatory if Category is filled")
    name = ""
    unique_id = ""

# Submit button
if st.button("Submit"):
    if input_choice == "Category" and not category_level:
        st.error("Category Level is mandatory when Category is filled.")
    else:
        if input_choice == "Name":
            get_by_name(name)
        elif input_choice == "UniqueID":
            get_by_uniqueid(unique_id)
        elif input_choice == "Category":
            cat_level(category, category_level)
