import streamlit as st
import pandas as pd

df = pd.read_csv(\
	'https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv'\
	, parse_dates=True\
	, header=0\
	, index_col=0)

df2 = pd.read_csv(\
	'https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv'\
	, parse_dates=True\
	, header=0\
	, index_col=0)
df2.drop(columns=["ALL"],inplace = True)

st.bar_chart(df)
st.bar_chart(df2)