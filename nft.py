import streamlit as st
import requests
import json

endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
st.header(f"OpenSea NFT API Explorer - {endpoint}")

#st.sidebar.write("the thing")

if endpoint == 'Assets':
    params = {
        'collection': 'the-wanderers',
        'limit': 1
    }

    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

    st.write(r.json())
