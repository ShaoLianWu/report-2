import streamlit as st  
def BostonCeltics():
  st.header('Boston Celtics')
  st.write('Boston Celtics(1946年-至今)')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "22  次")
  col2.metric("分組冠軍🏆", "32  次")
  st.write('波士頓塞爾蒂克隊的英文隊名為Boston Celtics，成立於1946年，目前所在地區是美國麻塞諸塞州波士頓市，主場為TD北岸花園球館，為美國職籃史上獲得總冠軍次數最多的球隊。')
