import streamlit as st
import requests
import json
from web3 import Web3
import pandas as pd

endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
st.header(f"OpenSea NFT API Explorer - {endpoint}")

st.sidebar.subheader("Filters")

collection = st.sidebar.text_input("Collection")
owner = st.sidebar.text_input("Owner")

if endpoint == 'Assets':
    params = {}

    if collection:
        params['collection'] = collection
    if owner:
        params['owner'] = owner

    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

    response = r.json()

    for asset in response["assets"]:
        if asset['name']:
            st.write(asset['name'])
        else=
            st.write(f"{asset['collection']['name']} #{asset['token_id']}")

        if asset['image_url'].endswith("mp4") or asset['image_url'].endswith('mov'):
            st.video(asset['image_url'])
        else:
            st.image(asset['image_url'])

    st.write(r.json())
