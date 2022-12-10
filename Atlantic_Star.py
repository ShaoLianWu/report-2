import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl
def BostonCeltics_Star():
  st.header('Boston Celtics三大傳奇球星')
  option=st.selectbox('選擇球星？',['Bill Russell', 'Larry Bird', 'Paul Pierce'])
  if option=='Bill Russell':
    image = Image.open('star/guardians.jpg')
    st.image(image) 
    df = pd.read_excel("star/Atlantic_Central_Star.xlsx",sheet_name="工作表1",usecols="A:H")
    new_df = df[0:1]
    st.dataframe(new_df)
  else:
      image = Image.open('star/傳奇球星.jpg')
      st.image(image) 
    
   
      

