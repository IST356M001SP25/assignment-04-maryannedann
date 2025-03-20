import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal Data Browser")

uploaded_file = st.file_uploader("Upload a data file (CSV, Excel, or JSON)", type=["csv", "xlsx", "xls", "json"])

if uploaded_file:
    ext = pl.get_file_extension(uploaded_file.name)
    df = pl.load_file(uploaded_file, ext)
    
    st.subheader("Data Preview")
    st.dataframe(df)
    
    st.subheader("Column Names")
    st.write(pl.get_column_names(df))
    
    dtype_options = {"Object": "object", "Integer": "int64", "Float": "float64"}
    selected_dtype = st.selectbox("Select column type to filter", list(dtype_options.keys()))
    
    if selected_dtype:
        st.subheader(f"Columns of type {selected_dtype}")
        st.write(pl.get_columns_of_type(df, dtype_options[selected_dtype]))
    
    selected_column = st.selectbox("Select a column to view unique values", df.columns)
    
    if selected_column:
        st.subheader(f"Unique Values in {selected_column}")
        st.write(pl.get_unique_values(df, selected_column))
