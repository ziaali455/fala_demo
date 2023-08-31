import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="🗣 Fala")
with st.sidebar:
    st.title('🗣 Fala')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']