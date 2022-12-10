import streamlit as st  
from PIL import Image

def BostonCeltics_Star():
  image = Image.open('star/傳奇球星.jpg')
  st.image(image) 
  option=st.selectbox('選擇球星？',['Bill Russell', 'Larry Bird', 'Paul Pierce'])

