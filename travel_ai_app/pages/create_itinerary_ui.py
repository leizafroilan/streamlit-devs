import streamlit as st
import os
from time import sleep
from get_itinerary import get_itinerary

css_style = """
    <style>
        .parent-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative; 
            padding 10px;
        }
        .top-row {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 100%;
        }
        .bottom-row {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 100%;
        }
        .column1 {
            padding: 10px 10px 10px 0px;
            line-height: 1;
        }
        .column1 h3 {
            font-size: 20px;
            color: blue;
            font-weight: bold;
        }
        .column1 p {
            font-size: 14px;
            font-weight: bold;
            font-style: italic;
        }
         .column2 {
            padding: 10px 10px 10px 0px;
            border-right: 2px solid blue;
        }
        .column3 {
            padding: 10px;
        }
        .column4 {
            margin: auto 0;
            height: 100%;
            flex-direction: column;
            justify-content: center;
            padding-left: 10px; 
        }
        .image-container {
            width: 300px; 
            height: 200px; 
            border: 2px solid #ccc;
            border-radius: 10px
            overflow: hidden;
            position: relative;
        }

        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover; 
            position: absolute;
            text-align: center;
            top: 0;
            left: 0;
        }        
    .disclaimer {
        background-color: #f8d7da; /* Light red background */
        color: #721c24; /* Dark red text color */
        border: 1px solid #f5c6cb; /* Red border */
        padding: 15px;
        margin-bottom: 20px; /* Add some space below the disclaimer */
        border-radius: 4px; /* Rounded corners */
    }
    .disclaimer h3 {
        font-size: 16px;
    }
    .disclaimer p {
        margin: 0; /* Remove default margins for paragraphs */
        font-size: 14px; /* Adjust font size */
        line-height: 1.5; /* Adjust line height for readability */
    }
    @media (max-width: 540px) {
        .parent-container  {
            padding: 0;
        }
        .top-row {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            width: 100%;
        }
        .bottom-row {
            display: flex;
            justify-content: center; 
            align-items: center; 
            flex-direction: column;
}
        }
        .column1 {
            padding: 0;
            line-height: 1;
        }
        .column2 {
            border-right: 0;
            padding: 0px 0px 10px 0px;
        }
        .column4 {
            border-top: 2px solid blue;
            padding: 10px 0px 0px 0px;
        }
        .image-container {
            display: flex; /* Add this */
            justify-content: center; /* Add this */
            align-items: center; /* Add this */
        }

        .image-container img {
            max-width: 100%; /* Change width to max-width */
            max-height: 100%; /* Change height to max-height */
            object-fit: cover; 
        }
    }
    </style>
    """


def toggle_hide():
    st.session_state.boolean = True

def toggle_show():
    st.session_state.boolean = False
    st.session_state.boolean = False
    st.session_state.city = None
    st.session_state.days = None
    st.session_state.view = None
    st.session_state.mode = None
    st.session_state.count = 0

def forms():

    st.markdown(css_style, unsafe_allow_html=True)
    st.sidebar.page_link("main.py", label="Home")
    st.sidebar.page_link("pages/create_itinerary_ui.py", label="Create Itinerary")
    st.sidebar.page_link("pages/about.py", label="About this App")


    if "boolean" not in st.session_state:
        st.session_state.boolean = False
    if "city" not in st.session_state:
        st.session_state.city = None
    if "days" not in st.session_state:
        st.session_state.days = None
    if "view" not in st.session_state:
        st.session_state.view = None
    if "mode" not in st.session_state:
        st.session_state.mode = None
    if "count" not in st.session_state:
        st.session_state.count = 0
    

    if not st.session_state.boolean:
        st.header(":blue[Prepare for Adventure with your AI buddy]", divider="blue")
        st.write("")
        city = st.text_input("City", value="", key="city")
        days = st.number_input("Days of Adventure", min_value=1, max_value=7, step=1, key="days")
        view = st.selectbox("Choose your scenic vibe", ["Urban", "Nature", "Historical", "Beach", "Parks"], key="view")
        mode = st.selectbox("Your travel companions?", ["Alone", "Couple", "Family"], key="mode")
        st.write("")
        button = st.button("Plan my trip", 
                    on_click=toggle_hide, 
                    disabled= False if city else True 
                    )
    else:
        
        city = st.session_state.city
        days = st.session_state.days
        view = st.session_state.view
        mode = st.session_state.mode

        with st.spinner(":blue[Brace yourselves, the adventure blueprint is coming together... ]"):
            try:
                locations = get_itinerary(city, days, mode, view)
                st.session_state.count = 0
            except Exception as e:
                if st.session_state.count < 2:
                    st.session_state.count +=1
                    locations = get_itinerary(city, days, mode, view)
                else:
                    st.write(":red[Failed to retrieve]")
                    st.write(e)
                    sleep(5)
                    toggle_show()
                exit(1)
        
        placeholder = st.empty()
        
       
        st.header(":blue[The roadmap to your adventures!]", divider="blue")
        st.write("")
        st.subheader(city)
        st.write(locations["summary"])

        for location in locations["itinerary"]:
            st.write("")
            st.markdown(f"""<div class='parent-container'>
                                <div class="top-row">
                                    <div class='column1'>
                                        <h3>{location['title']}</h3>
                                        <p>Distance: {location['distance']}</p>
                                    </div> 
                                        <div class='column3'> 
                                    </div>
                                </div>
                                <div class="bottom-row">
                                    <div class='column2'>
                                        <div class="image-container">
                                                <img src={location["photo"]} >
                                        </div>
                                    </div>                         
                                    <div class='column4'>
                                        {location["review"]}
                                    </div>  
                                </div>  
                            """, unsafe_allow_html=True)   
        st.write("")
        st.write("")
        st.markdown("""<div class='disclaimer'>
                    <h3>Disclaimer:<h3>
                    <p>
                    Users are advised to exercise caution and independently verify any information provided by this platform, including but not limited to transportation schedules, accommodation details, and attraction operating hours. Factors such as weather conditions, local events, and unforeseen circumstances may impact the feasibility and availability of certain activities suggested in your itinerary
                    </p>
                    </div>""", unsafe_allow_html=True) 

        st.write("")
        st.write("")
        button = st.button("Start Over", 
                on_click=toggle_show,
                disabled= False
                    )
                
forms()
