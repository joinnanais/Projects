import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# Set up the landing page

st.set_page_config(
    page_title= "Sales Dashboard",
    page_icon= ":bar_chart:",
    layout = "wide"
)


#Create a file path
csv_file_path = 'C:\\Users\\joinna.patiag\\OneDrive - Elemis Ltd\\Documents\\Scripts\\Sprint 13\\Sample - Superstore.csv'

#Read csv file and select encoding 
df = pd.read_csv(csv_file_path, encoding='latin1')

#Print dataframe
print(df)