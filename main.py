import streamlit as st
import numpy as np
import pandas as pd

df1 = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv', parse_dates=True, index_col=0)
df2 = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/death_total.csv', parse_dates=True, index_col=0)



df = pd.merge(df1, df2, on='日付')

df.to_csv("merged.csv", index=False)

# インタラクティブ
#st.dataframe(df.style.highlight_max(axis=0),width=400,height=400)

# 静的
# st.table(df.style.highlight_max(axis=0))



#st.line_chart(df)
st.area_chart(df1)

st.area_chart(df2)

#st.bar_chart(df)
st.dataframe(df.style.highlight_max(axis=0),width=400,height=400)