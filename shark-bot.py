import logging
import discord
from datetime import datetime
from dbConnect import dbConnect
import os


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

DATABASE_URL = os.environ['DATABASE_URL']
CLIENT_TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

def insertRowIntoDb(row):
    db = dbConnect(DATABASE_URL)
    conn = db.initConnection()
    cur = db.initCursor(conn)
    db.insertMessageRow(cur, conn, row)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def createMentionString(message):
    return message.author.mention


@client.event
async def on_message(message):

    server_id = message.guild.id
    server_name = message.guild.name
    channel = message.channel.id
    user_id = message.author.id
    curr_username = message.author.name
    user_disciminator = message.author.discriminator
    msg = message.content
    members = client.get_guild(server_id).members
    member = [member for member in members if member.id == user_id]  
    user_join_time = str(member[0].joined_at)
    message_timestamp = str(message.created_at)
    msg_id = message.id
 
    
    row = {
        'server_id': str(server_id),
        'server_name': str(server_name),
        'channel': str(channel),
        'user_id': str(user_id),
        'curr_username': str(curr_username),
        'user_disciminator': str(user_disciminator),
        'message': str(msg),
        'user_join_time': str(user_join_time),
        'message_timestamp': str(message_timestamp),
        'msg_id': str(msg_id)
    }
        
    insertRowIntoDb(row)

    if message.content.startswith('$mentionMe'):
        print(message.author)
        print(msg)
        await message.channel.send(createMentionString(message))

client.run(CLIENT_TOKEN)
