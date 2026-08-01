"""
Fahamu AI 254

Main Application Entry Point
"""

import streamlit as st

from ui.styles import load_css
from ui.components import (
    hero,
    footer,
)
from ui.sidebar import render_sidebar
from ui.chat import render_chat


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Fahamu AI 254",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LOAD CUSTOM STYLES
# ==========================================================

load_css()

# ==========================================================
# SIDEBAR
# ==========================================================

render_sidebar()

# ==========================================================
# MAIN PAGE
# ==========================================================

hero()

render_chat()

footer()