import streamlit as st
st.write("Good morning")
st.write("Hello!")

import urllib.request

with urllib.request.urlopen('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv') as u:
  st.write(u.info())
  st.write(u.read())

