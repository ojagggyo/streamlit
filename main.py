
import streamlit as st
import json

st.write (
        "%s(%s);" % ("callback", json.dumps({"name":"hogehoge"} )))