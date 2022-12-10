import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl
def BostonCeltics_Star():
  st.header('Boston Celtics三大傳奇球星')
  df = pd.read_excel("star/Atlantic_Central_Star.xlsx",sheet_name="工作表1",usecols="A:H")  
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('star/傳奇球星.jpg')
    st.image(image)
  with col2:
    option=st.selectbox('選擇球星？',['Bill Russell', 'Larry Bird', 'Paul Pierce'])
    if option=='Bill Russell':
      new_df = df[0:1]
      st.dataframe(new_df)
    if option=='Larry Bird':
      new_df = df[1:2]
      st.dataframe(new_df)
    if option=='Paul Pierce':
      new_df = df[2:3]
      st.dataframe(new_df)
    
   
   
      

