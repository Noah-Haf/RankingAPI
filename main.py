from fastapi import FastAPI
import os
import requests
from ro_py.client import Client
from dotenv import load_dotenv
import asyncio
load_dotenv()

RobloxCookie = os.getenv("COOKIE")
APIKEY = os.getenv("API_KEY")


client = Client(RobloxCookie)

app = FastAPI()


@app.get("/group/promote/")
async def read_items(user_name: str, key: str,groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.promote()
     return ("The user was promoted!")
    else:
        return "Incorrect key"

@app.get("/group/demote/")
async def read_items(user_name: str, key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.demote()
     return ("The user was demoted!")
    else:
        return "Incorrect key"

@app.get("/group/rank/")
async def read_items(user_name: str, key: str, groupid: int, rankid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.change_rank(rankid)
     return ("The user had their ranked changed")
    else:
        return "Incorrect key"
    
