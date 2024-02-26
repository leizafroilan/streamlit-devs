import streamlit as st

css_style = """
    <style>
        .about-desc {
            font-size: 16px;
        }
        .powered-by {
            font-size: 18px;
            font-weight: bold;
            padding: 50px 0 5px 0;
        }
        .technologies {
            list-style-type: none;
            display: block;
            padding: 0;
        }
        .technologies a {
            text-decoration: none;
            color: #007BFF;
        }
        .technologies a:hover {
            text-decoration: underline;
        }
        .built-with {
            font-size: 16px;
            padding: 20px 0px 20px 0px;
        }
    </style>
    """

def about():

    st.session_state.boolean = False
    st.session_state.boolean = False
    st.session_state.city = None
    st.session_state.days = None
    st.session_state.view = None
    st.session_state.mode = None
    st.session_state.count = 0

    st.header(":blue[About this App]", divider="blue")
    st.sidebar.page_link("main.py", label="Home")
    st.sidebar.page_link("pages/create_itinerary_ui.py", label="Create Itinerary")
    st.sidebar.page_link("pages/about.py", label="About this App")
    st.write("")
    st.markdown(css_style, unsafe_allow_html=True)
    st.markdown("""  
                    <p> This website offers a platform for users to create travel itineraries using automated tools and artificial intelligence. While we strive to provide accurate and helpful suggestions for your travel plans, it is important to note that the information generated may not always be entirely accurate or reflective of current conditions.

Users are advised to exercise caution and independently verify any information provided by this platform, including but not limited to transportation schedules, accommodation details, and attraction operating hours. Factors such as weather conditions, local events, and unforeseen circumstances may impact the feasibility and availability of certain activities suggested in your itinerary.

Additionally, users should always consult official travel advisories, local authorities, and reputable sources for the latest updates on travel restrictions, safety guidelines, and entry requirements for their intended destinations.

By using this website to create your travel itinerary, you acknowledge and accept that the information provided is for informational purposes only and that the website and its operators shall not be held liable for any inaccuracies, omissions, or adverse experiences resulting from reliance on the generated content.

Travel responsibly and enjoy your journey!
                    </p>
                    <p class="powered-by">Powered by:</p>
                    <div class="technologies">
                        <p>
                            <a href="https://langchain.com" target="_blank">LangChain 🚀</a>
                        </p>
                        <p>
                            <a href="https://openai.com" target="_blank">OpenAI 🧠</a>
                        </p>
                    <div>
                    <p class="built-with">Built with <a href="https://streamlit.io" target="_blank">Streamlit  🌐</a> by your <a href="mailto:no@email.com" target="_blank">Travel Agent AI</a></p>

    """, unsafe_allow_html=True)

about()