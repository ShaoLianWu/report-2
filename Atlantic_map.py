import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def BostonCeltics_map():
    st.header('主場:TD花園')
    col1, col2 = st.columns(2)
    with col1:
        
        TDGarden= folium.Map(location=[42.36622394101576, -71.06214665765047], zoom_start=16)
            # add marker for Liberty Bell
        tooltip = "TD花園"
        folium.Marker([42.36622394101576, -71.06214665765047], popup="TD花園", tooltip=tooltip
        ).add_to(TDGarden)
        folium_static(TDGarden)
        st.write("""### 地址：100 Legends Way, Boston, MA 02114美國,觀眾席數：18624席""")
    
    with col2:
        image = Image.open('Home/TD Garden.jpg')
        st.image(image)              
        image1 = Image.open('Home/TD Garden1.jpg')
        st.image(image1)
    
  
def BrooklynNets_map():
    st.header('主場:巴克萊中心')
    BarclaysCenter= folium.Map(location=[40.682725423383374, -73.97526212020857], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "巴克萊中心"
    folium.Marker([40.682725423383374, -73.97526212020857], popup="巴克萊中心", tooltip=tooltip
    ).add_to(BarclaysCenter)
    folium_static(BarclaysCenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Home/Barclays Center.jpg')       
        st.image(image)
    with col2:
        image1 =Image.open('Home/Barclays Center1.jpg')
        st.image(image1)
    st.write('地址：620 Atlantic Ave, Brooklyn, NY 11217美國,觀眾席數：17732席')
    
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
