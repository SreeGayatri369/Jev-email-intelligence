import streamlit as st

from dashboard import analyze_inbox

st.set_page_config(
    page_title="JEV Email Intelligence",
    layout="wide"
)

st.title(
    "📧 JEV Email Intelligence Platform"
)

st.write(
    "Real-time Gmail analysis using JEV"
)

if st.button("Analyze Inbox"):

    with st.spinner(
        "Analyzing emails..."
    ):

        df = analyze_inbox()

        st.dataframe(
            df,
            use_container_width=True
        )