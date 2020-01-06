import re
import random
import os

# Static defininitions
hello = ['Hi!', 'Hallo!', 'Wie gehts.', 'Ich grüße sie!', 'Was geht?', 'Guten Morgen']


# Event handlers

async def hi(message):
    if re.match("(?i).*(h+i+|h+a+l+o+).*", message.content) and not message.author.bot:
        await message.channel.send(random.choice(hello))


async def kick(message):
    if 'DISCORD_KICK' in os.environ and str(message.author.id) in os.environ['DISCORD_KICK']:
        await message.author.kick()


async def i_see_u(message):
    if random.randint(1, 20) == 1:
        await message.author.send("Ich sehe dich!")
