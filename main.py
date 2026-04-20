import streamlit as st
import warnings
warnings.filterwarnings("ignore")

pg = st.navigation([
    st.Page("home.py", title="Home"),
    st.Page("app.py", title="Score Predictor"),
    st.Page("app1.py", title="Match Predictor")
])

pg.run()