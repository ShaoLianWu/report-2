import streamlit as st
import folium    
from streamlit_folium import folium_static 
def BostonCeltics_map():
    col1, col2 = st.columns(2)
    with col1:
        st.header('主場:多倫多道明銀行花園')
        st.write('地址：100 Legends Way, Boston, Massachusetts, 02114')
        st.write('觀眾席數：18624席')
        image = Image.open('Home/TD Garden.png')
        st.image(image)
    with col2:
        TD Garden= folium.Map(location=[42.2159, 71.344], zoom_start=16)
        # add marker for Liberty Bell
        tooltip = "臺中洲際棒球場"
        folium.Marker([42.2159, 71.344], popup="臺中洲際棒球場", tooltip=tooltip
        ).add_to(TD Garden)
        folium_static(TD Garden)
