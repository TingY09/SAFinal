import streamlit as st
import numpy as np
import pandas as pd

# Draw a histogram
chart_data1 = pd.read_csv('compare.csv')
st.subheader('經濟與犯罪率的相關性')
st.scatter_chart(chart_data1, x='種類', y=['經濟成長率', '失業率'])
