import discord
import os
import commands


class OurCoolBot(discord.Client):

    async def on_ready(self):
        print('Logged in as {0}!'.format(self.user))
        game = discord.Game(os.environ['DISCORD_GAME'] if 'DISCORD_GAME' in os.environ else "Drive Them Right")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        await commands.hi(message)
        await commands.kick(message)


client = OurCoolBot()
if 'DISCORD_TOKEN' not in os.environ:
    print("Give Discord Token via DISCORD_TOKEN")
else:
    client.run(os.environ['DISCORD_TOKEN'])
