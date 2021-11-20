#This application is built by dzikamai matereke
#Github: 
#linkedin:  


'''this is build using the following libraries: 
streamlit: https://streamlit.io/ an opem source platform for creating and sharing custom web apps for machine learning and data science with python.
plotly.graph_objects: https://plotly.com/python-api-reference/generated/plotly.graph_objects.Bar.html#id5 a graphing library for creating charts and graphics
'''
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import requests

def main():
    
    st.title("Analysis of Health Care costs borne by Health Co.")   
    try:
        #Will update this to use an S3 bucket to pull data from
        #r = requests.get('https://streamlitdatabucket.s3.ap-southeast-2.amazonaws.com/health.xlsx?AWSAccessKeyId=AKIASLYPYXU7MNLRRE2V&Expires=1637390104&Signature=p22bHaDj19fKpGqXSaSdj9dfhyk%3D')
        df = pd.read_excel('C:\\Users\\deema\\OneDrive\\Documents\\GitHub\\Streamlit-Data-Analysis-Webapp\\datafile\\health.xlsx')
        st.dataframe(df)
    finally:
        st.write("Import function has failed")

    

    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Home", "Descriptive Analytics", "Predictice Analytics")
    )
if __name__=='__main__':
    main()