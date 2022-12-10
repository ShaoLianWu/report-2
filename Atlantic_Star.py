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
  df = pd.read_excel("star/Atlantic_Central_Star.xlsx",sheet_name="工作表1",usecols="球員,出賽,投籃命中率,三分命中率,罰球命中率,總籃板,總助攻,總得分")
  st.write(df)

