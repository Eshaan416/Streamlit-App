import streamlit as st
import pandas as pd

conn = st.connection("postgresql", "sql")

# Function to retrieve data using category and category level
@st.cache_data
def cat_level(category, category_level):
    res = conn.query(
        "SELECT items.uid,items.img,items.title FROM items, categories WHERE categories.level = :c AND categories.name = :d AND items.uid = categories.uid;",
        params=dict(c=category_level, d=category)
    )
    st.write(res)
    for index,row in res.iterrows():
        get_by_uniqueid(row['uid'])

        

# Function to retrieve data using name
@st.cache_data
def get_by_name(title):
    res = conn.query(
        "SELECT items.uid,items.img,items.title,ARRAY_AGG(categories.name) as categories_field FROM items,categories WHERE items.title = :n AND items.uid=categories.uid GROUP BY items.uid;",
        params=dict(n=title)
    )
    for index,row in res.iterrows():
        st.divider()
        st.title(row['title'])
        col1,col2=st.columns(2)
        
        col1.image(row['img'])
        col1.write({row['uid']})
        level=1
        col2.header("category fields")
        for category in row['categories_field']:
            col2.write(level)
            col2.write(category)
            col2.divider()
            level+=1

# Function to retrieve data using uniqueid
@st.cache_data
def get_by_uniqueid(uid):
    res = conn.query(
        "SELECT items.uid,items.img,items.title,ARRAY_AGG(categories.name) as categories_field FROM items,categories WHERE items.uid = :u and categories.uid=items.uid GROUP BY items.uid",
        params=dict(u=uid)
    )
    for index,row in res.iterrows():
        st.divider()
        st.title(row['title'])
        col1,col2=st.columns(2)
        
        col1.image(row['img'])
        col1.write({row['uid']})
        level=1
        col2.header("category fields")
        for category in row['categories_field']:
            col2.write(level)
            col2.write(category)
            col2.divider()
            level+=1

