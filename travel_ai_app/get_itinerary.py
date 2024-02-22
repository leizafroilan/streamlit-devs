from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import json
from time import sleep
from img_getter import brave_search
from records import create_records, get_records


def get_itinerary(city, days, mode, view):
    load_dotenv()

    llm = OpenAI(model_name="gpt-3.5-turbo-instruct",
                    temperature=0, 
                    max_tokens = 3072)


    template = """

        This following needs t o be in json format with key - summary
        ----
        Provide a brief summary or description of the {location}
        ----

        The following should be on json format with keys - itinerary, day, location, 
        photo (leave it blank/empty), review, distance
        ----
        Provide an itinerary based on the {location} for a {days}-day trip.
        Traveller is traveling {mode} and wants to see 
        {view}. Make a section for each day and location, then provide a detailed description of each section.
        Provide distance (how many minutes) from the last location to the new location with means of transportation 
        if possible. Make the distance more descriptive and include directions how to get to the location'
        ----

        Max token is 3072, adjust output to 3072 tokens if it exceeds. 

        Consider the demography of the location, if distance between locations cannot be reached by bus 
        in 1 day, exclude the location
    """


    prompt = PromptTemplate(input_variables=["location","days", "mode", "view"],
                                template=template)
    chain = LLMChain(llm=llm, prompt=prompt, output_key="review")

    raw_summary = chain.invoke({"location": city, "days": days, "mode": mode, "view": view})

    summary = json.loads(raw_summary["review"])
    
    for index, loc in enumerate(summary["itinerary"]):

        img = get_records(loc["location"])

        if not img:
            print(f"image not found for {loc['location']}")
            img = brave_search(loc["location"]) 
            # create_records(loc["location"], img)
            sleep(2)

        summary["itinerary"][index]["photo"] = img

    return summary
