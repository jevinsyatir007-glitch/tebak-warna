from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tebak Warna Foto", page_icon="🎨", layout="centered")

st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding-top: 0.5rem; padding-bottom: 0; max-width: 820px;}
      .stApp {background: #FFF8EC;}
    </style>
    """,
    unsafe_allow_html=True,
)

game_html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(game_html, height=1150, scrolling=True)
