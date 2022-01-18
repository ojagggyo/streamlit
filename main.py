import streamlit as st
st.write("Good morning")
st.write("Hello!")

import os
st.write(os.getcwd())

#import urllib.request
#with urllib.request.urlopen('https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv') as u:
#  st.write(u.info())
#  s = u.read()
#  st.write("<br>".join(s.decode('utf-8').split('\r\n')))