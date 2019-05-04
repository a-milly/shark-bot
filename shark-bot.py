import logging
import discord
import asyncio
from datetime import datetime
from threading import Timer



logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = discord.Client()

leaderboard = {}

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, resetLeaderBoard)
t.start()

def resetLeaderBoard():
    leaderboard = {}
    return leaderboard

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def createMentionString(message):
    return message.author.mention

def messageCounter(message):

    author = createMentionString(message)
    channel = message.channel

    if(author not in leaderboard):
        leaderboard[author] = 1
    else:
        leaderboard[author] += 1
    
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse = True)

    msg = messageFormater(sorted_leaderboard)

    return msg

def messageFormater(leaderboard):
    counter = 1
    msg_string = ''
    for author in leaderboard:
        msg_string += str(counter) +': ' + author[0] + '- ' + str(author[1]) + ' messages' + '\n'
        counter += 1
    return msg_string

@client.event
async def on_message(message):
    msg = messageCounter(message)
    print(msg)

    if message.content.startswith('$topDaily'):
        print(message.author)
        print(msg)
        await message.channel.send(msg)



    # elif message.content.startswith('!sleep'):
    #     await asyncio.sleep(5)
    #     await client.send_message(message.channel, 'Done sleeping')

client.run('MzE4MTI5NzAzNzgzMjM1NTg1.DAuDww.uMMplmx_Mr7xp-jIO8ZV1O44NL4')