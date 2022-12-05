import streamlit as st  
import Atlantic 
import Central
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇區域？', ['Atlantic', 'Central', 'Southeast', 'Northwest','Pacific','Southwest'])
if option=='Atlantic':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'])
  if teams=='Boston Celtics':
    Atlantic.BostonCeltics()
  if teams=='Brooklyn Nets':
    Atlantic.BrooklynNets()
  if teams=='New York Knicks':
    Atlantic.NewYorkKnicks()  
  if teams=='Philadelphia 76ers':
    Atlantic.Philadelphia76ers() 
  if teams=='Toronto Raptors':
    Atlantic.TorontoRaptors()
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
    
    
