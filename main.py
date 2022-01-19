import streamlit as st
#simport numpy as np
import pandas as pd

df1 = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv', parse_dates=True, header=0, index_col=0)
df2 = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/death_total.csv', parse_dates=True, header=0, index_col=0)

for i, name in reversed(list(enumerate(df2["死亡者数"].to_list()))):
	if i < 1 : break
	df2["死亡者数"][i] = df2["死亡者数"][i] - df2["死亡者数"][i-1]   

st.area_chart(df1)
st.area_chart(df2)

df = pd.merge(df1, df2, on='日付')
st.area_chart(df)

st.dataframe(df1,width=400,height=400)
st.dataframe(df2,width=400,height=400)
st.dataframe(df,width=400,height=400)



