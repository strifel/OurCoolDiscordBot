import re
import random

# Static defininitions
hello = ['Hi!', 'Hallo!', 'Wie gehts.', 'Ich grüße sie!', 'Was geht?', 'Guten Morgen']


# Event handlers

async def hi(message):
    if re.match("(?i).*(h+i+|h+a+l+o+).*", message.content) and not message.author.bot:
        await message.channel.send(random.choice(hello))
