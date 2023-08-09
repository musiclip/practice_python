import streamlit as st
from page import intro as intro
from page import project as p
from page import project1 as p1
from page import project2 as p2
from page import project3 as p3
from page import project4 as p4
from page import project5 as p5



st.title('Streamlit library')

item_list = ['item_intro','item0','item1','item2', 'item3','item4','item5']

item_labels = {'item_intro':'설명','item0':'st.dataframe','item1':'st.pyplot','item2':'st.button','item3':'st.text_input','item4':'st.header/title/write','item5':'folium_static()'}

FIL = lambda x : item_labels[x]
item = st.sidebar.selectbox('목록을 선택하세요.', item_list, format_func = FIL)

if item == 'item_intro':
    intro.app()
elif item == 'item0':
    p.app()
elif item == 'item1':
    p1.app()
elif item == 'item2':
    p2.app()
elif item == 'item3':
    p3.app()
elif item == 'item4':
    p4.app()
elif item == 'item5':
    p5.app()
