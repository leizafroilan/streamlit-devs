import pandas as pd
import os
from datetime import datetime


# filepath = os.path.join(os.getcwd(), "files", "records.csv")
filepath = os.path.join("/mount/src/streamlit-devs", "files", "records.csv")

def create_records(location: str, image: str):
    
    df = pd.read_csv(filepath)
    data =  df.to_dict(orient='records')
    

    for d in data:
        entry = str(d["location"])
        if location.lower() in entry.lower():
            return 

    new_data = {"location": location, "image": image, "age": datetime.now()}
    data.append(new_data)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    

def get_records(location: str):

    df = pd.read_csv(filepath)
    data =  df.to_dict(orient='records')

    for d in data:
        entry = str(d["location"])
        if location.lower() == entry.lower():
            return d["image"]

    return None    

