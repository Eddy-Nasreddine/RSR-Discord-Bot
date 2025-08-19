from datetime import date
import discord
from User import User
from Items import Item


def ItemEmbed(member, user:User, item:Item) -> discord.Embed:
    author = member.nick
    avatar = member.avatar
    user_points = user.get_points()
    item_cost = item.cost
    embed = discord.Embed(
    title = item.name,
    description="Would you like to purchase this item?",
    color=0x9900ff)
    embed.add_field(name="Costs    \u200b", value=item_cost, inline=True)
    embed.add_field(name="Dockets    \u200b", value=user_points, inline=True)
    embed.set_footer(text = f"Requested by {author}", icon_url= avatar)
    return embed

def embed_message_start(member, op_type):
    embed = discord.Embed(
    title = f"Beginning Attendance ({op_type})",
    description = "Attendance is starting click 'here' to verify your attendance!",
    colour= discord.Colour.blue(),
    )
    embed.set_footer(text = f"Started by {member.nick}", icon_url=member.avatar)
    return embed

def embed_message_end(bot_url=None, interaction=None):
    embed = discord.Embed(
    title = "Closing Attendance...",
    description = "You can no longer attend this session!",
    colour= discord.Colour.red(),
    )
    if (bot_url is not None):
        embed.set_footer(text = f"Attendance has been automatically closed due to timeout.", icon_url=bot_url)
    else:
        user = interaction.user
        embed.set_footer(text = f"Ended by {user.nick}", icon_url= user.avatar)
    return embed

def embed_attendees(attendees_nick):
    members_str = "```"
    for member in attendees_nick:
        members_str+= f"{member}\n"
    members_str += "```"
    embed = discord.Embed(
        title=f"Attendees({len(attendees_nick)}) :raised_hand:",
        color=0xff9500,
        description=members_str)
    embed.set_footer(text=f"{date.today().strftime('%Y-%m-%d')}")
    attendees_nick = []
    return embed

def item_refund_embed(member, item:Item, user: User):
    author = member.nick
    avatar = member.avatar
    item_cost = item.cost
    points = user.get_points()
    embed = discord.Embed(
    title = item.name,
    description="Would you like to refund this item?",
    color=0xfbff00)
    embed.add_field(name="Refund    \u200b", value=item_cost, inline=True)
    embed.add_field(name="Points    \u200b", value=points, inline=True)
    embed.add_field(name="Remaining Points", value=points + item_cost, inline=True)
    embed.set_footer(text = f"Requested by {author}", icon_url= avatar)
    return embed

def embed_op_type(member):
    embed = discord.Embed(
    title = "Op type",
    description = "Select the type of op you have started.",
    colour= discord.Colour.blue(),
    )
    embed.set_footer(text = f"Started by {member.nick}", icon_url= member.avatar)
    return embed