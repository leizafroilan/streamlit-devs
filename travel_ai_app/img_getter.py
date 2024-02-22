from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain_openai import OpenAI
from dotenv import load_dotenv
import requests
import json
import os

def brave_search(image: str):
    api_key = "BSA3zaxKaiuR4M-5F3BOna-6lFSfWnW"
    url = "https://api.search.brave.com/res/v1/images/search"
    placeholder = "https://placeholder-no-img.jpg"

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key
        }

    params = { "q": image,
        "search_lang": "en",
        "count": 1
        }

    try:
        res = requests.get(url, headers=headers, params=params)
        img = json.loads(res.text)
        img = img["results"][0]["properties"]["url"]
        return img
    except Exception as e:
        return placeholder
    

# def pixabay_search(image: str):

#     load_dotenv()
#     placeholder = "https://placeholder-no-img.jpg"
    
#     # search = DuckDuckGoSearchRun(backend="images")
    
#     # res = search.run("Provide url in .jpg for Sentosa")
#     # print(res)
#     pixabay_api = "42447354-004e50c144b118151f58364ab"
    
#     params = {"key": pixabay_api, 
#                 "q": image, 
#                 "image_type": "photo",
#                 "category": "travel",
#                 "per_page": 3}

#     result = requests.get("https://pixabay.com/api/", params=params).json()

#     try:
#         img = result["hits"][0]["webformatURL"]
#         return placeholder if not img else img
#     except Exception as e:
#         return placeholder


