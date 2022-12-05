import streamlit as st  
import ATLANTIC 
import Central
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['ATLANTIC', 'Central', '東南組', '西北組','太平洋組','西南組'])
if option=='ATLANTIC':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'])
  if teams=='Boston Celtics':
    ATLANTIC.BostonCeltics()
  if teams=='Brooklyn Nets':
    ATLANTIC.BrooklynNets()
  if teams=='New York Knicks':
    ATLANTIC.NewYorkKnicks()  
  if teams=='Philadelphia 76ers':
    ATLANTIC.Philadelphia76ers() 
  if teams=='Toronto Raptors':
    ATLANTIC.TorontoRaptors()
if option=='Central':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks'])
  if teams=='Chicago Bulls':
    Central.ChicagoBulls()
  if teams=='Cleveland Cavaliers':
    Central.ClevelandCavaliers()
  if teams=='Detroit Pistons':
    Central.DetroitPistons()  
  if teams=='Indiana Pacers':
    Central.IndianaPacers() 
  if teams=='Milwaukee Bucks':
    Central.MilwaukeeBucks()
    
    
