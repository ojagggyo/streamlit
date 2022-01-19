import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv')
# df = pd.DataFrame({
# 	'1列目':[1,2,3,4],
# 	'2列目':[10,20,30,40],
# })

#df

st.dataframe(df)