import difflib
import json
from Items import store
from Items import Item
from constants import ADMIN_ROLE_ID
from discord import Interaction
def find_closest_item(query: str) -> Item:
    items = []
    for item in store.values():
        items.append(item.name)
    matches = difflib.get_close_matches(query, items, n=1, cutoff=0.0)
    return store[matches[0]]

def open_json():
    with open("members.json", "r") as json_file:
        json_data = json_file.read()
    return json.loads(json_data)
    
def write_json(id, row):
    members = open_json()
    members[str(id)] = {"row": row}
    with open("members.json", "w") as f:
        json.dump(members, f, indent=4)

def is_zues(member) -> bool:
    role_ids = [role.id for role in member.roles]
    return ADMIN_ROLE_ID in role_ids

def is_linked(id:int) -> bool:
    if str(id) not in open_json():
        return False
    return True