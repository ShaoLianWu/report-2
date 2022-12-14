import streamlit as st  
from PIL import Image
import pandas as pd
import xlrd  
import openpyxl
df = pd.read_excel("star/Atlantic_Central_Star.xlsx",sheet_name="工作表1",usecols="A:H") 
def BostonCeltics_Star():
  st.header('Boston Celtics三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
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
  with col2:
    if option=='Bill Russell':
      image = Image.open('star/Bill Russell.jpg')
      st.image(image)
    if option=='Larry Bird':
      image = Image.open('star/Larry Bird.jpg')
      st.image(image)
    if option=='Paul Pierce':
      image = Image.open('star/Paul Pierce.jpg')
      st.image(image)
def BrooklynNets_Star():
  st.header('Brooklyn Nets三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Julius Erving', 'Jason Kidd', 'Derrick Coleman'])
    if option=='Julius Erving':
      new_df = df[5:6]
      st.dataframe(new_df)
    if option=='Jason Kidd':
      new_df = df[6:7]
      st.dataframe(new_df)
    if option=='Derrick Coleman':
      new_df = df[7:8]
      st.dataframe(new_df)
  with col2:
    if option=='Julius Erving':
      image = Image.open('star/Julius Erving.jpg')
      st.image(image)
    if option=='Jason Kidd':
      image = Image.open('star/Jason Kidd.jpg')
      st.image(image)
    if option=='Derrick Coleman':
      image = Image.open('star/Derrick Coleman.jpg')
      st.image(image)
def NewYorkKnicks_Star():
  st.header('New York Knicks三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Walt Frazier', 'Patrick Ewing', 'Willis Reed'])
    if option=='Walt Frazier':
      new_df = df[9:10]
      st.dataframe(new_df)
    if option=='Patrick Ewing':
      new_df = df[10:11]
      st.dataframe(new_df)
    if option=='Willis Reed':
      new_df = df[11:12]
      st.dataframe(new_df)
  with col2:
    if option=='Walt Frazier':
      image = Image.open('star/Walt Frazier.jpg')
      st.image(image)
    if option=='Patrick Ewing':
      image = Image.open('star/Patrick Ewing.jpg')
      st.image(image)
    if option=='Willis Reed':
      image = Image.open('star/Willis Reed.jpg')
      st.image(image)
def Philadelphia76ers_Star():
  st.header('Philadelphia 76ers三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Dikembe Mutombo', 'Allen Iverson', 'Wilt Chamberlain'])
    if option=='Dikembe Mutombo':
      new_df = df[13:14]
      st.dataframe(new_df)
    if option=='Allen Iverson':
      new_df = df[14:15]
      st.dataframe(new_df)
    if option=='Wilt Chamberlain':
      new_df = df[15:16]
      st.dataframe(new_df)
  with col2:
    if option=='Dikembe Mutombo':
      image = Image.open('star/Dikembe Mutombo.jpg')
      st.image(image)
    if option=='Allen Iverson':
      image = Image.open('star/Allen Iverson.jpg')
      st.image(image)
    if option=='Willis Reed':
      image = Image.open('star/Wilt Chamberlain.jpg')
      st.image(image)
def TorontoRaptors_Star():
  st.header('Toronto Raptors三大傳奇球星')
  col1, col2 = st.columns(2)
  with col1:
    option=st.selectbox('選擇球星？',['Kyle Lowry', 'Chris Bosh', 'Vince Carter'])
    if option=='Kyle Lowry':
      new_df = df[17:18]
      st.dataframe(new_df)
    if option=='Chris Bosh':
      new_df = df[18:19]
      st.dataframe(new_df)
    if option=='Vince Carter':
      new_df = df[19:20]
      st.dataframe(new_df)
  with col2:
    if option=='Kyle Lowry':
      image = Image.open('star/Kyle Lowry.jpg')
      st.image(image)
    if option=='Chris Bosh':
      image = Image.open('star/Chris Bosh.jpg')
      st.image(image)
    if option=='Vince Carter':
      image = Image.open('star/Vince Carter.jpg')
      st.image(image)      
    
  
      

