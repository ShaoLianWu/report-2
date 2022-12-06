import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def ChicagoBulls_map():
    st.header('主場:聯合中心球館')
    UnitedCenter= folium.Map(location=[41.880708350972725, -87.67417027269533], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "聯合中心球館"
    folium.Marker([41.880708350972725, -87.67417027269533], popup="聯合中心球館", tooltip=tooltip
    ).add_to(UnitedCenter)
    folium_static(UnitedCenter)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('Home/United Center.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('Home/United Center1.png')
        st.image(image1)
    st.write('地址：1901 W Madison St, Chicago, IL 60612美國,觀眾席數：21879席')
  
def ClevelandCavaliers_map():
    st.header('主場:快貸球館')
    QuickenLoansArena= folium.Map(location=[41.49661457628494, -81.68800263971569], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "快貸球館"
    folium.Marker([41.49661457628494, -81.68800263971569], popup="快貸球館", tooltip=tooltip
    ).add_to(QuickenLoansArena)
    folium_static(QuickenLoansArena)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Home/Quicken Loans Arena.jpg')       
        st.image(image)
    with col2:
        image1 =Image.open('Home/Quicken Loans Arena1.jpg')
        st.image(image1)
    st.write('地址：1 Center Court, Cleveland, OH 44115美國,觀眾席數：20562席')
    
def NewYorkKnicks_map():
    st.header('主場:麥迪遜廣場花園')
    MSGTheGarden= folium.Map(location=[40.7505, -73.99352], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "麥迪遜廣場花園"
    folium.Marker([40.7505, -73.99352], popup="麥迪遜廣場花園", tooltip=tooltip
    ).add_to(MSGTheGarden)
    folium_static(MSGTheGarden)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Home/MSGTheGarden.jpg')       
        st.image(image)
    with col2:
        image1 =Image.open('Home/MSGTheGarden1.jpg')
        st.image(image1)
    st.write('地址：4 Pennsylvania Plaza, New York, NY 10001美國,觀眾席數：19812席')

def Philadelphia76ers_map():
    st.header('主場:富國銀行中心')
    wellsfargocenter= folium.Map(location=[39.90130024709659, -75.17162545031324], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "富國銀行中心"
    folium.Marker([39.90130024709659, -75.17162545031324], popup="富國銀行中心", tooltip=tooltip
    ).add_to(wellsfargocenter)
    folium_static(wellsfargocenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Home/wellsfargocenter.jpg')       
        st.image(image)
    with col2:
        image1 =Image.open('Home/wellsfargocenter1.jpg')
        st.image(image1)
    st.write('地址：3601 S Broad St, Philadelphia, PA 19148美國,觀眾席數：21000席')

def TorontoRaptors_map():
    st.header('主場:豐業銀行體育館')
    ScotiabankArena= folium.Map(location=[43.643485488886185, -79.37908251728793], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "豐業銀行體育館"
    folium.Marker([43.643485488886185, -79.37908251728793], popup="豐業銀行體育館", tooltip=tooltip
    ).add_to(ScotiabankArena)
    folium_static(ScotiabankArena)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Home/ScotiabankArena.jpg')       
        st.image(image)
    with col2:
        image1 =Image.open('Home/ScotiabankArena1.jpg')
        st.image(image1)
    st.write('地址：40 Bay St., Toronto, ON M5J 2X2加拿大,觀眾席數：19800席')    
