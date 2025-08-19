import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") # The bot token
GUILD_ID = int(os.getenv("GUILD_ID")) # The discord server ID
SHEET_ID = str(os.getenv("SHEET_ID")) # Google Sheets ID"
ATTENDENCE_CHAT_ID = 1383345000175374447 # The channel ID for attendance
ATTENDANCE_TIMEOUT = 1800 # Time before attendance session times out if not ended manually
ADMIN_ROLE_ID = 1356133972802928880 # The role ID for Zeus 
DOCKET_AMOUNT_MAIN = 75 # The amount of points given for attending a main session
DOCKET_AMOUNT_SIDE = 35 # The amount of points given for attending a side session
BOT_ADMINS_IDS = [216147553857568769, 431962855261208577]  # List of role IDs that can use /Add command
USER_NOT_LINKED = "Unable to use commands until you have linked your account using /link." 
RANK_ROW = "B"
DOCKETS_ROW = "D"
REFUND_ROW = "E"
ITEMS_ROW = "N"
TOTAL_ROW = "K"
