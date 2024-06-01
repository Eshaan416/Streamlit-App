import streamlit as st 
import pandas as pd

# Title of the app
st.title("Input Form")

# Input fields
name = st.text_input("Name")
unique_id = st.text_input("UniqueID")
category = st.text_input("Category")
category_level = None

# If category is filled, category level becomes mandatory
if category:
    category_level = st.text_input("Category Level", "This field is mandatory if Category is filled")

#File Uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_json(uploaded_file)
    st.write(dataframe)

# Submit button
if st.button("Submit"):
    if not category and not category_level:
        st.success(f"Submitted:\nName: {name}\nUniqueID: {unique_id}\nCategory: {category}\nCategory Level: {category_level}")
    elif category and not category_level:
        st.error("Category Level is mandatory when Category is filled.")
    else:
        st.success(f"Submitted:\nName: {name}\nUniqueID: {unique_id}\nCategory: {category}\nCategory Level: {category_level}")
    
