import streamlit as st
import pandas as pd

st.write("PCR陽性")
df = pd.read_csv(\
	'https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv'\
	, parse_dates=True\
	, index_col=0)
st.bar_chart(df)

st.write("死亡者")
df2 = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/death_total.csv'\
	, parse_dates=True\
	, index_col=0)
# 累計を日ごとの値に変換する。
for i, name in reversed(list(enumerate(df2["死亡者数"].to_list()))):
	if i < 1 : break
	df2["死亡者数"][i] = df2["死亡者数"][i] - df2["死亡者数"][i-1]   
st.bar_chart(df2)