import streamlit as st


def main():
    st.markdown(
            """
            <style>
            .sidebar-content div[data-testid="stSidebar"][aria-expanded="false"] > div:last-child > div > div:last-child {
                display: none;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    st.header(":blue[Travel Agent AI]", divider="blue")
    st.sidebar.page_link("main.py", label="Home")
    st.sidebar.page_link("pages/create_itinerary_ui.py", label="Create Itinerary")
    st.sidebar.page_link("pages/about.py", label="About this App")

main()

