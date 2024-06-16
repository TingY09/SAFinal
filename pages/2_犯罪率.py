import streamlit as st
import numpy as np
import pandas as pd

# Draw a histogram
chart_data = pd.read_csv('crimeTime.csv')
st.subheader('竊盜')
st.line_chart(chart_data, x = "年度", y=['重大竊盜', '普通竊盜', '汽車竊盜', '機車竊盜'])

st.subheader('傷害、妨害自由及詐欺')
st.line_chart(chart_data, x = "年度", y=['重傷害', '一般傷害', '妨害自由', '詐欺'])

st.subheader('其他')
st.line_chart(chart_data, x = "年度", y=['贓物', '賭博', '背信', '重利'])