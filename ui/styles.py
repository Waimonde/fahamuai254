"""
UI Styles for Fahamu AI 254
"""

import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ----------------------------------------------------
GENERAL
-----------------------------------------------------*/

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container{
    max-width:1300px;
    padding-top:2rem;
    padding-bottom:1rem;
}

html, body, [class*="css"]{
    font-family: "Segoe UI", sans-serif;
    background-color:#F7F9FC;
}


/* ----------------------------------------------------
HEADINGS
-----------------------------------------------------*/

.main-title{
    font-size:52px;
    font-weight:800;
    color:#0B6E4F;
    margin-bottom:0;
}

.sub-title{
    font-size:22px;
    color:#555;
    margin-top:-5px;
}

.author{
    font-size:16px;
    color:#888;
    margin-top:8px;
    margin-bottom:25px;
}


/* ----------------------------------------------------
SIDEBAR
-----------------------------------------------------*/

section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E5E7EB;
}

.sidebar-title{
    font-size:22px;
    font-weight:bold;
    color:#0B6E4F;
}

.sidebar-section{
    margin-top:20px;
}


/* ----------------------------------------------------
CHAT BUBBLES
-----------------------------------------------------*/

.user-card{
    background:#DCF8C6;
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
}

.ai-card{
    background:#FFFFFF;
    padding:18px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #E5E7EB;
    box-shadow:0 2px 10px rgba(0,0,0,0.05);
}


/* ----------------------------------------------------
SOURCE CARD
-----------------------------------------------------*/

.source-card{

    background:#F8F9FA;

    border-left:5px solid #0B6E4F;

    padding:10px;

    margin-top:8px;

    border-radius:8px;

}


/* ----------------------------------------------------
BUTTONS
-----------------------------------------------------*/

div.stButton > button{

    width:100%;

    height:48px;

    border-radius:10px;

    border:none;

    background:#0B6E4F;

    color:white;

    font-size:17px;

    font-weight:bold;

}

div.stButton > button:hover{

    background:#084C38;

    color:white;

}


/* ----------------------------------------------------
UPLOAD
-----------------------------------------------------*/

[data-testid="stFileUploader"]{

    border:2px dashed #0B6E4F;

    border-radius:12px;

    padding:10px;

}


/* ----------------------------------------------------
CHAT INPUT
-----------------------------------------------------*/

[data-testid="stChatInput"]{

    border-radius:12px;

}


/* ----------------------------------------------------
FOOTER
-----------------------------------------------------*/

.footer{

    margin-top:70px;

    text-align:center;

    color:#777;

    font-size:14px;

    border-top:1px solid #DDD;

    padding-top:15px;

}


/* ----------------------------------------------------
WELCOME CARD
-----------------------------------------------------*/

.welcome{

    background:white;

    border-radius:15px;

    padding:25px;

    border:1px solid #E5E7EB;

    box-shadow:0 2px 12px rgba(0,0,0,.05);

    margin-bottom:20px;

}

</style>
""",
        unsafe_allow_html=True,
    )