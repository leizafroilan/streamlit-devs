from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import streamlit as st
import os
from time import sleep
from schemas import Summary
from img_getter import brave_search
from records import create_records, get_records


def get_itinerary(city, days, mode, view):
    load_dotenv()

    os.environ["OPENAI_API_KEY"] = st.secrets["my_secrets"]["OPENAI_API_KEY"]

    llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                    temperature=1, 
                    max_tokens = 3072)

    parser = PydanticOutputParser(pydantic_object=Summary)

    temp = []

    template = """
        Provide a brief summary/historical and current events of the {location} 
        
        Provide an itinerary based on the {location} for a {days}-day trip.
        Traveller is traveling {mode} and wants to see {view}. 
        Make a section for each day and location, then provide a detailed description of each section.
        Provide distance (how many minutes) and directions how to get to the new location 
        with means of transportation if possible. 
        Make the distance more descriptive.

        Consider the demography of the location, if distance between locations cannot be reached by bus 
        in 6 hours, exclude the location.
        
        Provide these as if you are a tourist guide
        \n{format_instructions}\n
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["location", "days", "mode", "view"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    
    # And a query intended to prompt a language model to populate the data structure.
    prompt_and_model = prompt | llm
    output = prompt_and_model.invoke({
                                "location": city, 
                                "days": days, 
                                "mode": mode,
                                "view": view
                                })
    summary = parser.invoke(output)
    print(summary)
    for loc in summary.details:

        img = get_records(loc.location)

        if not img:
            print(f"image not found for {loc.location}")
            img = brave_search(loc.location) 
            # create_records(loc.location, img)
            sleep(2)

        entry = {
              "title": f"{loc.day} - {loc.location}",
              "distance": loc.distance,
              "review": loc.review,
              "photo": img
            }
        temp.append(entry)
    
    payload = {"summary": summary.summary, "itinerary": temp}

    return payload




