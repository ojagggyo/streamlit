import streamlit as st
#import numpy as np
import pandas as pd

df = pd.read_csv('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv',header=0)

# インタラクティブ
#st.dataframe(df.style.highlight_max(axis=0),width=400,height=400)

# 静的
# st.table(df.style.highlight_max(axis=0))



#st.line_chart(df)
st.area_chart(df)