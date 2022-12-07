import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def DenverNuggets_map():
    st.header('主場:波爾體育館')
    BallArena= folium.Map(location=[39.749843021630504, -105.00794625648932], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "波爾體育館"
    folium.Marker([39.749843021630504, -105.00794625648932], popup="波爾體育館", tooltip=tooltip
    ).add_to(BallArena)
    folium_static(BallArena)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('Ball Arena .jpeg')
        st.image(image)        
    with col2:        
        image1 = Image.open('Ball Arena 1.jpeg')
        st.image(image1)
    st.write('地址：1000 Chopper Cir, Denver, CO 80204美國,觀眾席數：19,155席')
  
def MinnesotaTimberwolves_map():
    st.header('主場:標靶中心')
    TargetCenter= folium.Map(location=[44.98006909117457, -93.2760948230289], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "標靶中心"
    folium.Marker([44.98006909117457, -93.2760948230289], popup="標靶中心", tooltip=tooltip
    ).add_to(TargetCenter)
    folium_static(TargetCenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Target Center.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Target Center1.jpeg')
        st.image(image1)
    st.write('地址：600 N 1st Ave, Minneapolis, MN 55403美國,觀眾席數：18,798席')
def OklahomCityThunder_map():
    st.header('主場:切薩皮克能源球館')
    ChesapeakeEnergyArena= folium.Map(location=[35.46412251164774, -97.51519977239266], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "切薩皮克能源球館"
    folium.Marker([35.46412251164774, -97.51519977239266], popup="切薩皮克能源球館", tooltip=tooltip
    ).add_to(ChesapeakeEnergyArena)
    folium_static(ChesapeakeEnergyArena)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Chesapeake Energy Arena .jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Chesapeake Energy Arena1.jpeg')
        st.image(image1)
    st.write('地址：100 W Reno Ave, Oklahoma City, OK 73102美國,觀眾席數：18,203席')
def PortlandTrailBlazers_map():
    st.header('主場:摩達中心')
    ModaCenter= folium.Map(location=[45.53222514229469, -122.6669282525212], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "摩達中心"
    folium.Marker([45.53222514229469, -122.6669282525212], popup="摩達中心", tooltip=tooltip
    ).add_to(ModaCenter)
    folium_static(ModaCenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Moda Center.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Moda Center1.jpeg')
        st.image(image1)
    st.write('地址：1 N Center Ct St, Portland, OR 97227美國,觀眾席數：20,630席')
def UtahJazz_map():
    st.header('主場:生活智能家居球館')
    VivintArena= folium.Map(location=[40.76950185004792, -111.9012591931141], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "生活智能家居球館"
    folium.Marker([40.76950185004792, -111.9012591931141], popup="生活智能家居球館", tooltip=tooltip
    ).add_to(VivintArena)
    folium_static(VivintArena)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Vivint Arena.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Vivint Arena1.jpeg')
        st.image(image1)
    st.write('地址：301 S Temple, Salt Lake City, UT 84101美國,觀眾席數：20,000席')
