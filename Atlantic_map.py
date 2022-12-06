import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def BostonCeltics_map():
    col1, col2 = st.columns(2)
    with col1:
        st.header('主場:TD花園')
        st.write('地址：100 Legends Way, Boston, Massachusetts, 02114')
        st.write('觀眾席數：18624席')
        image = Image.open('Home/TD Garden.jpg')
        image = Image.open('Home/TD Garden1.jpg')
        st.image(image)
        st.image(image)
    with col2:
        TDGarden= folium.Map(location=[42.36622394101576, -71.06214665765047], zoom_start=16)
        # add marker for Liberty Bell
        tooltip = "TD花園"
        folium.Marker([42.36622394101576, -71.06214665765047], popup="TD花園", tooltip=tooltip
        ).add_to(TDGarden)
        folium_static(TDGarden)
