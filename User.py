
import json
from google_sheets import get_values, update_sheet
from Items import Item
from constants import SHEET_ID, RANK_ROW, DOCKETS_ROW, REFUND_ROW, ITEMS_ROW, TOTAL_ROW

with open("members.json", "r") as json_file:
    json_data = json_file.read()
members = json.loads(json_data)

class User:
    def __init__(self, id):
        self.row = members[str(id)]["row"]
        self.id = id
        
    def get_points(self) -> int:
        return int(get_values(SHEET_ID, f'{DOCKETS_ROW}{self.row}:{DOCKETS_ROW}{self.row}')[0][0])
 
    def can_afford(self, cost: int) -> bool:
        if self.get_points() >= cost:
            return True
        else:
            return False
        
    def get_rank(self) -> str:
        return get_values(SHEET_ID, f'{RANK_ROW}{self.row}:{RANK_ROW}{self.row}')[0][0]
    
    def get_attendance_total(self):
        return get_values(SHEET_ID, f'{TOTAL_ROW}{self.row}:{TOTAL_ROW}{self.row}')[0][0]

    def get_items(self):
        items_str = get_values(SHEET_ID, f'{ITEMS_ROW}{self.row}:{ITEMS_ROW}{self.row}')
        if not items_str:
            return []
        return [item.strip() for item in items_str[0][0].split(",")]
    
    def has_item(self, item) -> bool:
        return item in self.get_items()
    
    def add_to_total(self):
        new_total = int(self.get_attendance_total()) + 1
        update_sheet(SHEET_ID, f'{TOTAL_ROW}{self.row}:{TOTAL_ROW}{self.row}', new_total)

    def can_buy(self, item:Item) -> bool:
        if self.has_item(item.name):
            return False, f"You already own {item.name}."   
        if item.prerequisite is not None:
            if item.prerequisite not in self.get_items():
                return False, f"You need to own {item.prerequisite} before buying this item."
        if item.rank is not None:
            rank = self.get_rank()
            print(rank)
            print(item.rank)
            if rank not in item.rank:
                return False, f"You need to be {item.rank} to buy this item."
        if not self.can_afford(item.cost):
            return False, "You don't have enough points to buy this item."
        return True, None
    
    def add_points(self, points: int):
        current_points = self.get_points()
        new_points = current_points + points
        update_sheet(SHEET_ID, f'{DOCKETS_ROW}{self.row}:{DOCKETS_ROW}{self.row}', new_points)
    
    def buy_item(self, item: Item):
        points = self.get_points()
        new_points = points - item.cost
        update_sheet(SHEET_ID, f'{DOCKETS_ROW}{self.row}:{DOCKETS_ROW}{self.row}', new_points)
        try:
            items = self.get_items()
        except IndexError:
            items = []
        if not items or (len(items) == 1 and items[0] == ""):
            items = []
        items.append(item.name)
        items_str = ", ".join(i.strip() for i in items if i.strip())
        update_sheet(SHEET_ID, f'{ITEMS_ROW}{self.row}:{ITEMS_ROW}{self.row}', items_str)
        
    def refund_item(self, item: Item):
        points = self.get_points()
        new_points = points + item.cost
        update_sheet(SHEET_ID, f'{DOCKETS_ROW}{self.row}:{DOCKETS_ROW}{self.row}', new_points)
        items = self.get_items()
        items.remove(item.name)
        items_str = ", ".join(i.strip() for i in items if i.strip())
        update_sheet(SHEET_ID, f'{ITEMS_ROW}{self.row}:{ITEMS_ROW}{self.row}', items_str)
        update_sheet(SHEET_ID, f'{REFUND_ROW}{self.row}:{REFUND_ROW}{self.row}', 0)
    
        
    def can_refund(self, item: Item):
        if int(get_values(SHEET_ID, f'{REFUND_ROW}{self.row}:{REFUND_ROW}{self.row}')[0][0]) == 0:
            return False, "You have already used your refund for this month."
        if not self.has_item(item.name):
            return False, "You do not own this item."
        return True, None

  