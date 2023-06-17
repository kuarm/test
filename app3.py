import streamlit as st
from st_excel_table import Table

st.title("Streamlit-Excel-Table")

data = [
    {"id": "hoge", "x": 5.77, "y": 8.85, "color": "red"},
    {"id": "hogedb", "x": 15.77, "y": 18.85, "color": "red"},
    {"id": "hogeba", "x": 25.77, "y": 28.85, "color": "red"},
    {"id": "hogeas", "x": 35.77, "y": 38.85, "color": "red"},
]