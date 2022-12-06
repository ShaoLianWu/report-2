import streamlit as st  
import Atlantic 
import Central
import Southeast 
import Northwest
import Pacific 
import Southwest
import Atlantic_map #存取Atlantic_map.py
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇區域？', ['Atlantic', 'Central', 'Southeast', 'Northwest','Pacific','Southwest'])
if option=='Atlantic':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'])
  if teams=='Boston Celtics':
    Atlantic.BostonCeltics()
    Atlantic_map.BostonCeltics_map() #呼叫Atlantic_map.py裡的BostonCeltics_map()
  if teams=='Brooklyn Nets':
    Atlantic.BrooklynNets()
    Atlantic_map.BrooklynNets_map()
  if teams=='New York Knicks':
    Atlantic.NewYorkKnicks() 
    Atlantic_map.NewYorkKnicks_map()
  if teams=='Philadelphia 76ers':
    Atlantic.Philadelphia76ers() 
    Atlantic_map.Philadelphia76ers_map()
  if teams=='Toronto Raptors':
    Atlantic.TorontoRaptors()
    Atlantic_map.TorontoRaptors_map()
    
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
    
if option=='Pacific': 
  teams=st.sidebar.selectbox( '選擇球隊？', ['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'])
  if teams=='Golden State Warriors':
    Pacific.Golden_State_Warriors()
  if teams=='Los Angeles Clippers':
    Pacific.Los_Angeles_Clippers()
  if teams=='Los Angeles Lakers':
    Pacific.Los_Angeles_Lakers()
  if teams=='Phoenix Suns':
    Pacific.Phoenix_Suns()
  if teams=='Sacramento Kings':
    Pacific.Sacramento_Kings() 
    
if option=='Southwest':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs'])
  if teams=='Dallas Mavericks':
    Southwest.Dallas_Mavericks()
  if teams=='Houston Rockets':
    Southwest.Houston_Rockets()
  if teams=='Memphis Grizzlies':
    Southwest.Memphis_Grizzlies()
  if teams=='New Orleans Pelicans':
    Southwest.New_Orleans_Pelicans()
  if teams=='San Antonio Spurs':
    Southwest.San_Antonio_Spurs()
if option=='Southeast':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'])
  if teams=='Atlanta Hawks':
    Southeast.AtlantaHawks()
  if teams=='Charlotte Hornets':
    Southeast.CharlotteHornets()
  if teams=='Miami Heat':
    Southeast.MiamiHeat()
  if teams=='Orlando Magic':
    Southeast.OrlandoMagic()
  if teams=='Washington Wizards':
    Southeast.WashingtonWizards()
if option=='Northwest':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 'Portland Trail Blazers','Utah Jazz'])
  if teams=='Denver Nuggets':
    Northwest.DenverNuggets()  
  if teams=='Minnesota Timberwolves':
    Northwest.MinnesotaTimberwolves()
  if teams=='Oklahoma City Thunder':
    Northwest.OklahomCityThunder()
  if teams=='Portland Trail Blazers':
    Northwest.PortlandTrailBlazers()
  if teams=='Utah Jazz':
    Northwest.UtahJazz()
    
