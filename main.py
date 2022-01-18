import streamlit as st
st.write("Good morning")
st.write("Hello!")

import urllib.request

with urllib.request.urlopen('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv') as u:
  st.write(u.info())
  s = u.read()
st.write(s.decode('utf-8').split('\r\n').join('<br>'))