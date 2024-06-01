from sqlalchemy import text

import streamlit as st


def insert_data(df_items,df_categories):
    conn = st.connection('postgresql', 'sql')


    with conn.session as s:
        s.execute(text('DROP TABLE IF EXISTS categories;'))
        s.execute(text('DROP TABLE IF EXISTS items;'))
        s.execute(text('CREATE TABLE IF NOT EXISTS items (uid TEXT PRIMARY KEY,title TEXT,availability BOOLEAN,description TEXT, img TEXT,price INT,gender TEXT);'))
        s.execute(text('CREATE TABLE IF NOT EXISTS categories(uid TEXT,level int,name text,PRIMARY KEY(uid,level),FOREIGN KEY(uid) REFERENCES items(uid));'))
        
        for index,row in df_items.iterrows():
            s.execute(text('INSERT INTO items VALUES (:uid,:title,:availability,:description,:img,:price,:gender);'),
            params=dict(uid=row['uniqueId'],title=row['title'],availability=row['availability'],description=row['productDescription'],img=row['productImage'],price=row['price'],gender=row['gender']))
        for index,row in df_categories.iterrows():
            s.execute(text('INSERT INTO categories VALUES (:uid,:level,:category)'),
            params=dict(uid=row['uniqueId'],level=row['level'],category=row['cat']))
        s.commit()
