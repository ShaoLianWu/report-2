import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl
def BostonCeltics_Star():
  st.header('Boston Celtics三大傳奇球星')
  image = Image.open('star/傳奇球星.jpg')
  st.image(image) 
  option=st.selectbox('選擇球星？',['Bill Russell', 'Larry Bird', 'Paul Pierce'])
  df = pd.read_excel("star/Atlantic_Central_Star.xlsx",sheet_name="工作表1",usecols=[2,3,4,5,6,7])
  st.write(df)

