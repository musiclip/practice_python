import streamlit as st
from streamlit_folium import st_folium
import folium

m = folium.Map(location = [37.5602, 126.982], zoom_start = 12)
folium.Marker([37.542, 127.0565], popup = 'Liberty Bell', tooltip = 'Liberty Bell').add_to(m)

def desc():
    global m
    st_data = st_folium(m, width = 725)