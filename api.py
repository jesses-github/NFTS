from typing import Optional
from fastapi import FastAPI
from enum import Enum
import json
import pandas as pd
from typing import Optional
from terra_test import *
import os
from api_utilities import NFTDatabase
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

origins = ['http://localhost:3000']

class UsernameInput(str, Enum):
    sample_file = "sample_file"
    string_return = "Penis"
    one_thousand = 1000

json_path = 'sample_json2.json'
with open(json_path, 'r') as f: json_dict = json.load(f)
pull_links_json_path = 'api_pull_links.json'
with open(pull_links_json_path, 'r') as f: pull_links = json.load(f)
people = json_dict['people']
app = FastAPI()
folder = 'trashgang-site/src/Sample NFTs'
app.nft_db = NFTDatabase(folder)
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/other/{user_name}")
async def root(user_name):
    return {"Hello": user_name}

@app.get("/testing/{typed_input}")
async def root(typed_input: int):
    return {"Thanks for the int of": typed_input}

@app.get("/usernameconditional/{user_input}")
async def root(user_input: UsernameInput):
    if user_input == UsernameInput.sample_file: return json_dict
    if user_input == "Penis": return {"Hahaha": "A Penis"}
    if user_input == UsernameInput.one_thousand: return "You chose a thousand"

@app.get("/search/{username}")
async def root (username: str, gender: Optional[str] = None):
    dropped = []
    if not gender is None: 
        for i, person in enumerate(people):
            if gender != person['gender']: dropped.append(people.pop(i))
        # [people.pop(i) for i, person in enumerate(people) if person['gender'] != gender]
    for person in people:
        if person['firstName'] == username: return {"returned_value": person, "dropped_values": dropped, "remaining_people": people}

@app.get("/get_terra_address")
async def root (): return mk.acc_address

@app.get("/random_nft")
async def root ():
    app.nft_db.update_nfts_avaiable()
    if not app.nft_db.nfts_available: return "Currently out of stock - check back soon."
    paths = app.nft_db.get_random_nft_paths()
    if os.path.exists(paths[0]):
        # return (FileResponse(paths[0]), FileResponse(paths[1]))
        return FileResponse(paths[0])
    else:
        return {"error": "File not found."}

@app.get("/get_nft_links")
async def root(): return json.dumps(pull_links)

@app.get("/nftimage/{user_input}")
async def root(user_input):
    for k, v in pull_links.items():
        if user_input in str(k): return RedirectResponse(url=str(pull_links[k]))