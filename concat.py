import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import os
import json
from annotated_text import annotated_text
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly
import streamlit.components.v1 as components
import bar_chart_race as bcr
import base64
from datasets import load_dataset
import turtle as trt
import openpyxl






with st.sidebar:
    selected=option_menu(
        menu_title="Course of action",
        options=["Concatenation","QC Framework","Quality Chart","Track-up"],
        icons=["arrow-left-right","columns","graph-up-arrow","code-branch"],
        menu_icon="boxes",
        default_index=0,
        styles={
            "container":{"padding": "0!important","background-color":"azure"},
            "icon": {"color": "navy", "font-size": "25px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            }


        }
    )



#  Concatenation--------

if selected=="Concatenation":
    st.title(f"Concatenation")
    st.write("****Merge files in fastest way****") 
    
    
    options = ["First Sheet", "All Sheets"]
    pageopt=st.radio('****Concatenate by****', options)
    
    df=pd.DataFrame()

    
    
    if pageopt == "First Sheet":
        files = st.file_uploader(" ", type=["xls","xlsx","csv"], accept_multiple_files=True)
        for uploaded_file in files: 
            Tabel=pd.read_excel(uploaded_file)
            currentdf=pd.DataFrame(Tabel)
            print(currentdf)
            twoFrames = [df, currentdf]
            df=pd.concat(twoFrames)

    
    
    elif pageopt == "All Sheets":
        files = st.file_uploader(" ", type=["xls","xlsx","csv"], accept_multiple_files=True)
        
        for uploaded_file in files:
            if uploaded_file.name.endswith(".xlsx"):   
                new_file = openpyxl.load_workbook(uploaded_file)
                sheet_names = new_file.sheetnames
                for shet_name in sheet_names:    
                    Tabel=pd.read_excel(uploaded_file, sheet_name=shet_name)
                    currentdf=pd.DataFrame(Tabel)
                    print(currentdf)
                    twoFrames = [df, currentdf]
                    df=pd.concat(twoFrames)
            
    
    columnNames = []
    for colName in df.columns:
        columnNames.append(colName.strip().upper().replace("_", " "))

    df.columns = columnNames
    df=df.fillna('')
        
    
    st.info('''
    ****Note:****\n
    Can upload multiple excel files here. Every file should contains same format.\n
    ****What i do:****\n
    I will merge every files into a single file. Convert column names to uppercase and remove _ symbol. At the end return this consolidated file with CSV format.\n
    Once i done my work, U can see highlighted DOWNLOAD button. Then you can find your file on clicking DOWNLOAD button. 

    ''')

    dfshape=df.shape
    st.write(dfshape)

    convert=df.to_csv(index=False)

    st.download_button(
        label="Download",
        data=convert,
        file_name='Final_consolidation.csv',
        mime='text/csv',
    )
