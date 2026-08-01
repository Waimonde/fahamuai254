"""
Chat Interface for Fahamu AI 254
"""

import streamlit as st

from app.chat import chat_service
from ui.components import (
    welcome_card,
    suggested_questions,
    source_card,
    empty_chat,
)


def initialize_chat():
    """
    Initializes the session state.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "suggested_question" not in st.session_state:
        st.session_state.suggested_question = ""


def render_chat():

    initialize_chat()

    # -----------------------------------------------------
    # Welcome Screen
    # -----------------------------------------------------

    if len(st.session_state.messages) == 0:

        welcome_card()

        suggested_questions()

        st.divider()

        empty_chat()

    # -----------------------------------------------------
    # Display Chat History
    # -----------------------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant":

                sources = message.get("sources", [])

                if sources:

                    with st.expander("📚 Sources", expanded=False):

                        shown = set()

                        for doc in sources:

                            source = doc.metadata.get("source")
                            page = doc.metadata.get("page")

                            key = (source, page)

                            if key not in shown:

                                shown.add(key)

                                source_card(doc)

    # -----------------------------------------------------
    # Suggested Question Support
    # -----------------------------------------------------

    prompt = st.chat_input("Ask Fahamu AI 254...")

    if not prompt and st.session_state.suggested_question:

        prompt = st.session_state.suggested_question

        st.session_state.suggested_question = ""

    # -----------------------------------------------------
    # User Prompt
    # -----------------------------------------------------

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        # -------------------------------------------------
        # AI Response
        # -------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner("🤖 Fahamu is thinking..."):

                answer, sources = chat_service.ask(prompt)

            st.markdown(answer)

            if sources:

                with st.expander(
                    "📚 Sources",
                    expanded=False,
                ):

                    shown = set()

                    for doc in sources:

                        source = doc.metadata.get("source")
                        page = doc.metadata.get("page")

                        key = (source, page)

                        if key not in shown:

                            shown.add(key)

                            source_card(doc)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources,
            }
        )

        st.rerun()