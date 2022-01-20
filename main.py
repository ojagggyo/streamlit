import streamlit as st
import pandas as pd

df = pd.read_csv(\
	'https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv'\
	, parse_dates=True\
	, header=0\
	, index_col=0)

st.bar_chart(df)
