import streamlit as st  
from PIL import Image  
def ChicagoBulls():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Chicago Bulls.png')
    st.image(image) 
  with col2:
     st.title('Chicago Bulls')
     st.subheader('老闆:Michael Reinsdorf')
     st.subheader('GM:Marc Eversley')
     st.subheader('總教練:Billy Donovan')     
  st.write('芝加哥公牛(1966年-至今)') 
  st.write('芝加哥公牛隊的英文隊名為Chicago bulls，成立於1966年，目前所在城市是美國伊利諾州芝加哥（Chicago, Illinois），主場為聯合中心球館（United Center）。芝加哥是肉食加工業發達的城市，公牛對人們來說是力量的象徵，所以球隊以此命名。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "6  次")
  col2.metric("分組冠軍🏆", "6  次")   
def ClevelandCavaliers():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Cleveland Cavaliers.png')
    st.image(image) 
  with col2:
     st.title('Cleveland Cavaliers')
     st.subheader('老闆:Koby Altman')
     st.subheader('GM:Mike Gansey')
     st.subheader('總教練:J.B.Bickerstaff')     
  st.write('克里夫蘭騎士(1970年-至今)') 
  st.write('克里夫蘭騎士隊的英文隊名為Cleveland Cavaliers，球隊成立於1970年，目前所在城市是美國俄亥俄州克里夫蘭市(Cleveland, Ohio)，主場為速貸球館(Quicken Loans Arena)')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "1  次")
  col2.metric("分組冠軍🏆", "5  次")   
def DetroitPistons():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Detroit Pistons.png')
    st.image(image) 
  with col2:
     st.title('Detroit Pistons')
     st.subheader('老闆:Ed Stefanski')
     st.subheader('GM:Troy Weaver')
     st.subheader('總教練:Dwane Casey')     
  st.write('韋恩堡左納活塞（NBL）(1941年–1948年)-韋恩堡活塞（BAA）(1948年–1949年)-韋恩堡活塞（NBA）(1949年–1957年)-底特律活塞(1957年–至今)') 
  st.write('底特律活塞隊的英文隊名為Detroit Pistons，成立於1946年，目前所在地區是美國密歇根州底特律，主場為奧本山宮殿球場。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "3  次")
  col2.metric("分組冠軍🏆", "7  次")   
def IndianaPacers():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Indiana Pacers.png')
    st.image(image) 
  with col2:
     st.title('Indiana Pacers')
     st.subheader('老闆:Kevin Pritchard')
     st.subheader('GM:Chad Buchanan')
     st.subheader('總教練:Rick Carlisle')     
  st.write('印第安納溜馬（ABA）(1967年-1976年)-印第安納溜馬（NBA）(1976年-至今)')
  st.write('印第安那溜馬隊的英文隊名為Indiana Pacers，球隊成立於1976年，目前所在城市是美國印第安那州印第安納波里斯(Indianapolis, Indiana)，主場為銀行家生活球館(Bankers Life Fieldhouse)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "1  次")   
def MilwaukeeBucks():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('teams logo/Milwaukee Bucks.png')
    st.image(image) 
  with col2:
     st.title('Milwaukee Bucks')
     st.subheader('老闆:Peter Feigin')
     st.subheader('GM:Jon Horst')
     st.subheader('總教練:Mike Budenholzer')     
  st.write('密爾瓦基公鹿(1968年-至今)')
  st.write('密爾瓦基公鹿隊的英文隊名為Milwaukee Bucks，球隊成立於1968年，目前所在城市是美國威斯康辛州密爾瓦基市(Milwaukee, Wisconsin)，主場為布蘭德利中心球場(Bradley Center)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "2  次")
  col2.metric("分組冠軍🏆", "3  次")   
