import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

st.title("Housing Data Explorer")
st.write(
    """
    Welcome! This is the Home page for the housing data Streamlit app.
    Click the button below to open the main app page.
    """
)

if st.button("Open main app"):
    # Navigate to the app page in the pages folder.
    st.switch_page("pages/app.py")

st.caption("This app uses the housing dataset provided in the project repository.")
