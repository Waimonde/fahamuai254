"""
Sidebar UI for Fahamu AI 254
"""

import os
import streamlit as st

from ingest.ingest import ingestion_pipeline


KNOWLEDGE_BASE = "knowledge_base"


def _list_documents():
    """
    Returns a list of indexed PDF files.
    """

    if not os.path.exists(KNOWLEDGE_BASE):
        return []

    return sorted(
        [
            file
            for file in os.listdir(KNOWLEDGE_BASE)
            if file.lower().endswith(".pdf")
        ]
    )


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-title">
                📚 Knowledge Base
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        documents = _list_documents()

        st.markdown("### Indexed Documents")

        if documents:

            for document in documents:

                st.success(f"📄 {document}")

        else:

            st.info("No documents indexed.")

        st.divider()

        st.markdown("### Upload PDFs")

        uploaded_files = st.file_uploader(
            "Choose one or more PDF files",
            type=["pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed",
        )

        if st.button(
            "⚡ Build Knowledge Base",
            use_container_width=True,
        ):

            if not uploaded_files:

                st.warning("Please upload at least one PDF.")

            else:

                os.makedirs(KNOWLEDGE_BASE, exist_ok=True)

                progress = st.progress(0)

                status = st.empty()

                total = len(uploaded_files)

                for index, uploaded_file in enumerate(uploaded_files):

                    status.info(
                        f"Saving {uploaded_file.name}..."
                    )

                    save_path = os.path.join(
                        KNOWLEDGE_BASE,
                        uploaded_file.name,
                    )

                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    progress.progress(
                        (index + 1) / total
                    )

                status.info("Indexing documents...")

                with st.spinner("Building knowledge base..."):

                    ingestion_pipeline.run()

                progress.empty()

                status.empty()

                st.success(
                    "✅ Knowledge Base updated successfully."
                )

                st.rerun()

        st.divider()

        st.markdown("### Workspace")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🗑️ New Chat",
                use_container_width=True,
            ):

                st.session_state.messages = []

                st.rerun()

        with col2:

            if st.button(
                "🔄 Refresh",
                use_container_width=True,
            ):

                st.rerun()

        st.divider()

        st.markdown("### Statistics")

        st.metric(
            "Indexed PDFs",
            len(documents),
        )

        st.success("🟢 Local AI Ready")