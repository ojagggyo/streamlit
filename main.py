import streamlit as st
import pandas as pd

df1 = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv', parse_dates=True, header=0, index_col=0)
st.bar_chart(df1,use_container_width=True)