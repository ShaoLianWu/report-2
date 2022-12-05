import streamlit as st  
def BostonCeltics():
  st.header('Boston Celtics')
  st.write('Boston Celtics(1946年-至今)')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "22  次")
  col2.metric("分組冠軍🏆", "32  次")
