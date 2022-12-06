import streamlit as st  
from PIL import Image  
def DenverNuggets():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Denver Nuggets.png')
    st.image(image) 
  with col2:
     st.title('Denver Nuggets')
     st.subheader('老闆:Kroenke Sports & Entertainment')
     st.subheader('GM:Calvin Booth')
     st.subheader('總教練:Michael Malone')     
  st.write('丹佛火箭（ABA）(1967年-1974年)丹佛金塊（ABA）(1974年-1976年)丹佛金塊（NBA）(1976年-)') 
  st.write('丹佛金塊隊的英文隊名為Denver Nuggets，球隊成立於1967年，所在地區是美國科羅拉多州丹佛市(Denver, Colorado)，主場為百事中心。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "0  次")   
def MinnesotaTimberwolves():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Minnesota Timberwolves.jpeg')
    st.image(image) 
  with col2:
     st.title('Minnesota Timberwolves')
     st.subheader('老闆:Glen Taylor')
     st.subheader('GM:Tim Connelly')
     st.subheader('總教練:Chris Finch')     
  st.write('明尼蘇達灰狼(1989年-–至今）') 
  st.write('明尼蘇達灰狼隊的英文隊名為Minnesota Timberwolves，球隊成立於1989年，所在地區是美國明尼蘇達州明尼阿波利斯市(Minneapolis, Minnesota)，主場為標靶中心球館(Target Center)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "0  次")   
def OklahomCityThunder():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Oklahoma City Thunder.png')
    st.image(image) 
  with col2:
     st.title('Oklahoma City Thunder')
     st.subheader('老闆:Professional Basketball Club LLC (Clay Bennett, Chairman)')
     st.subheader('GM:Sam Presti')
     st.subheader('總教練:Mark Daigneault')     
  st.write('西雅圖超音速(1967年-2008年)俄克拉何馬城雷霆(2008年-現今)') 
  st.write('奧克拉荷馬雷霆隊的英文隊名為Oklahoma City Thunder，球隊成立於1967年，原名為西雅圖超音速隊，目前所在地區是美國奧克拉荷馬州奧克拉荷馬城(Oklahoma City, Oklahoma)，主場為切薩皮克能源球場(Chesapeake Energy Arena)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "1  次")
  col2.metric("分組冠軍🏆", "4  次")   
def PortlandTrailBlazers():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Portland Trail Blazers.png')
    st.image(image) 
  with col2:
     st.title('Portland Trail Blazers')
     st.subheader('老闆:Paul G. Allen Trust (Jody Allen, chairwoman)')
     st.subheader('GM:Joe Cronin')
     st.subheader('總教練:Chauncey Billups')     
  st.write('波特蘭开拓者 (1970–-至今)') 
  st.write('波特蘭拓荒者隊的英文隊名為Portland Trail Blazers，球隊成立於1970年，所在地區是美國俄勒岡州波特蘭市(Portland, Oregon)，主場為摩達中心(Moda Center)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "1  次")
  col2.metric("分組冠軍🏆", "3  次")    
def UtahJazz():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Utah Jazz.jpeg')
    st.image(image) 
  with col2:
     st.title('Utah Jazz')
     st.subheader('老闆:Ryan Smith')
     st.subheader('GM:Justin Zanik')
     st.subheader('總教練:Will Hardy')     
  st.write('紐奧良爵士(1974–1979)猶他爵士(1979年–-)') 
  st.write('猶他爵士隊的英文隊名為Utah Jazz，球隊成立於1974年，所在地區是美國猶他州鹽湖城，主場為能源方案球館。成立之初主場在紐奧良，是爵士樂的發源地，球隊也因此命名。1979年爵士隊主場移到猶他州鹽湖城，而隊名則繼續沿用至今。球隊剛建立的幾個賽季表現都不如人意，到1976年Elgin Baylor成為總教練後表現開始回穩，1983-1984年賽季爵士隊第一次打入季後賽，這一季中Adrian Delano Dantley球946次中投進813球，成為NBA史上第一位在第四節罰球得分超過800分的球員，至此以後爵士隊水準發揮穩定。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "2  次")   
