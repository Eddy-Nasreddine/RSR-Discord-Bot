from User import User
from Items import store, Item
from helper import find_closest_item
from google_sheets import update_sheet
a = User(216147553857568769)
# print(a.get_points())
# update_sheet("1cvyCENqDNLcNL1oNpNgHGwPw0iGZGxzZPeFj99FyezE", "D39:D39", "benbenben")

item = Item("Test Item", cost = 100)

# a.buy_item(item)
# a.add_points(1000)
print(a.get_items())
a.add_to_total()