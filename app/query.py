import streamlit as st
conn=st.connection("postgresql","sql")


def cat_level(category,category_level):
    res=conn.query(f"SELECT items.uid,items.title from items,categories where level=:c and name=:d and items.uid=categories.uid;",
                   params=dict(c=category_level,d=category))
    st.write(res)