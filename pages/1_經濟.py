import streamlit as st
import numpy as np
import pandas as pd

# Draw a histogram
chart_data = pd.read_csv('economy.csv')

tab1, tab2, tab3 = st.tabs(["平均每人國民所得與基本工資", "台灣經濟變化", "工資與工時"])

with tab1:
    st.subheader('平均每人國民所得與基本工資')
    st.line_chart(chart_data, x = "年度", y=['平均每人國民所得毛額（美元）', '基本工資（金額）-月薪'])

with tab2:
    st.subheader('台灣經濟變化')
    st.line_chart(chart_data, x = "年度", y=['經濟成長率', '儲蓄率', '失業率（百分比）', '消費者物價-指數', '消費者物價-年增率'])

with tab3:
    st.subheader('工資與工時')
    st.line_chart(chart_data, x = "年度", y=['基本工資（金額）-時薪', '工業及服務業平均月工時（小時）'])
