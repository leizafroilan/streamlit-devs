import streamlit as st


def main():

    st.session_state.boolean = False
    st.session_state.boolean = False
    st.session_state.city = None
    st.session_state.days = None
    st.session_state.view = None
    st.session_state.mode = None
    st.session_state.count = 0

    st.header(":blue[Travel Agent AI]", divider="blue")
    st.sidebar.page_link("main.py", label="Home")
    st.sidebar.page_link("pages/create_itinerary_ui.py", label="Create Itinerary")
    st.sidebar.page_link("pages/about.py", label="About this App")

main()

