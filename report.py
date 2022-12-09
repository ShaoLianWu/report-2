import streamlit as st  
import Atlantic 
import Central
import Southeast 
import Northwest
import Pacific 
import Southwest
import Atlantic_map#存取Atlantic_map.py
import Central_map
import Southeast_map
import Northwest_map
import Pacific_map
import 3star

st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇區域？', ['Atlantic', 'Central', 'Southeast', 'Northwest','Pacific','Southwest'])
if option=='Atlantic':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'])
  if teams=='Boston Celtics':
    Atlantic.BostonCeltics()
    3star.BostonCeltics_Star()
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
    Central_map.ChicagoBulls_map()
  if teams=='Cleveland Cavaliers':
    Central.ClevelandCavaliers()
    Central_map.ClevelandCavaliers_map()
  if teams=='Detroit Pistons':
    Central.DetroitPistons()  
    Central_map.DetroitPistons_map()
  if teams=='Indiana Pacers':
    Central.IndianaPacers() 
    Central_map.IndianaPacers_map()
  if teams=='Milwaukee Bucks':
    Central.MilwaukeeBucks()
    Central_map.MilwaukeeBucks_map()
if option=='Pacific': 
  teams=st.sidebar.selectbox( '選擇球隊？', ['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'])
  if teams=='Golden State Warriors':
    Pacific.Golden_State_Warriors() 
    Pacific_map.Golden_State_Warriors_map()
  if teams=='Los Angeles Clippers':
    Pacific.Los_Angeles_Clippers()
    Pacific_map.Los_Angeles_Clippers_map()
  if teams=='Los Angeles Lakers':
    Pacific.Los_Angeles_Lakers()    
    Pacific_map.Los_Angeles_Lakers_map()
  if teams=='Phoenix Suns':
    Pacific.Phoenix_Suns()
    Pacific_map.Phoenix_Suns_map()
  if teams=='Sacramento Kings':
    Pacific.Sacramento_Kings()     
    Pacific_map.Sacramento_Kings_map()
    
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
    Southeast_map.AtlantaHawks_map()
  if teams=='Charlotte Hornets':
    Southeast.CharlotteHornets()
    Southeast_map.CharlotteHornets_map()
  if teams=='Miami Heat':
    Southeast.MiamiHeat()
    Southeast_map.MiamiHeat_map()
  if teams=='Orlando Magic':
    Southeast.OrlandoMagic()
    Southeast_map.OrlandoMagic_map()
  if teams=='Washington Wizards':
    Southeast.WashingtonWizards()
    Southeast_map.WashingtonWizards_map()
if option=='Northwest':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 'Portland Trail Blazers','Utah Jazz'])
  if teams=='Denver Nuggets':
    Northwest.DenverNuggets() 
    Northwest_map.DenverNuggets_map() 
  if teams=='Minnesota Timberwolves':
    Northwest.MinnesotaTimberwolves()
    Northwest_map.MinnesotaTimberwolves_map() 
  if teams=='Oklahoma City Thunder':
    Northwest.OklahomCityThunder()
    Northwest_map.OklahomCityThunder_map() 
  if teams=='Portland Trail Blazers':
    Northwest.PortlandTrailBlazers()
    Northwest_map.PortlandTrailBlazers_map() 
  if teams=='Utah Jazz':
    Northwest.UtahJazz()
    Northwest_map.UtahJazz_map() 
    
