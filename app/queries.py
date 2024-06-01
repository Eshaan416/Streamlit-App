import streamlit as st

conn = st.connection("postgresql", "sql")

# Function to retrieve data using category and category level
def cat_level(category, category_level):
    res = conn.query(
        "SELECT items.uid, items.title FROM items, categories WHERE level = :c AND name = :d AND items.uid = categories.uid;",
        params=dict(c=category_level, d=category)
    )
    st.write(res)

# Function to retrieve data using name
def get_by_name(title):
    res = conn.query(
        "SELECT items.uid, items.title FROM items WHERE title = :n;",
        params=dict(n=title)
    )
    st.write(res)

# Function to retrieve data using uniqueid
def get_by_uniqueid(uid):
    res = conn.query(
        "SELECT items.uid, items.title FROM items WHERE uid = :u;",
        params=dict(u=uid)
    )
    st.write(res)
