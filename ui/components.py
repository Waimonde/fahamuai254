"""
Reusable UI Components for Fahamu AI 254
"""

import streamlit as st


# ============================================================
# HERO SECTION
# ============================================================

def hero():
    """
    Displays the application hero section.
    """

    st.markdown(
        """
        <div class="main-title">
            🇰🇪 Fahamu AI 254
        </div>

        <div class="sub-title">
            Your Private AI Knowledge Assistant
        </div>

        <div class="author">
            A Chat Bot by <b>David Maina Waimonde</b>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# WELCOME CARD
# ============================================================

def welcome_card():
    """
    Display welcome message.
    """

    st.markdown(
        """
        <div class="welcome">

        <h3>👋 Welcome!</h3>

        Ask questions about your uploaded documents.

        Fahamu AI only answers using the indexed knowledge base,
        helping reduce hallucinations and keeping responses grounded.

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SUGGESTED QUESTIONS
# ============================================================

def suggested_questions():

    st.markdown("### 💡 Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📄 What is personal data?",
            use_container_width=True,
            key="q1",
        ):
            st.session_state["suggested_question"] = (
                "What is personal data?"
            )

        if st.button(
            "⚖️ What are the rights of a data subject?",
            use_container_width=True,
            key="q2",
        ):
            st.session_state["suggested_question"] = (
                "What are the rights of a data subject?"
            )

    with col2:

        if st.button(
            "🏛️ Who is a data controller?",
            use_container_width=True,
            key="q3",
        ):
            st.session_state["suggested_question"] = (
                "Who is a data controller?"
            )

        if st.button(
            "📑 Summarize this document.",
            use_container_width=True,
            key="q4",
        ):
            st.session_state["suggested_question"] = (
                "Summarize this document."
            )


# ============================================================
# SOURCE CARD
# ============================================================

def source_card(doc):

    source = doc.metadata.get("source", "Unknown File")
    page = doc.metadata.get("page", "-")

    st.markdown(
        f"""
        <div class="source-card">

        📄 <b>{source}</b>

        <br>

        Page <b>{page}</b>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FOOTER
# ============================================================

def footer():

    st.markdown(
        """
        <div class="footer">

        <strong>Founder & CEO, Ryantech Solutions</strong>

        |

        Program Lead,
        <strong>Tu-Code Academy</strong>

        |

        Building & Scaling AI, Data Science &
        Software Solutions

        |

        Speaker

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# STATUS BADGE
# ============================================================

def status_badge():

    st.success("🟢 Local AI Ready")


# ============================================================
# EMPTY CHAT
# ============================================================

def empty_chat():

    st.info(
        "💬 Start by asking a question or upload a PDF and build your knowledge base."
    )