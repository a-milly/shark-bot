import logging
import discord
import asyncio

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = discord.Client()

leaderboard = {}

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

    if message.content.startswith('!test'):
    	# user = get_user_from_message(message)
        print(message.author)
        print(msg)
        await message.channel.send(msg)
    	# await client.send_message(message.channel,"dont't test me baka ")# + user.mention)
    	# await client.send_message(message.channel, 'dont be so loud ... baka' + ' @' + message.author.name)

    #     counter = 0
    #     tmp = await client.send_message(message.channel, 'Calculating messages...')
    #     async for log in client.logs_from(message.channel, limit=100):
    #         if log.author == message.author:
    #             counter += 1

    #     await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    # if len(message.content) >= 1:
    # 	await client.send_message(message.channel, 'dont be so loud ... baka' + ' @' + message.author.name)
    	# await client.send_message(message.channel, 'dont be so loud ... baka' + ' ' + discord.User(message.author).metnion())
    

    # elif message.content.startswith('!sleep'):
    #     await asyncio.sleep(5)
    #     await client.send_message(message.channel, 'Done sleeping')

client.run('MzE4MTI5NzAzNzgzMjM1NTg1.DAuDww.uMMplmx_Mr7xp-jIO8ZV1O44NL4')