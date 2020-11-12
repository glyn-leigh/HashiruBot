import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import find

load_dotenv()

print(discord.__version__)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
discord = discord
bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("Hashiru is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.startswith("hello"): 
		await message.channel.send("Did you need something?")


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}!'.format(guild.name))

bot.run(DISCORD_TOKEN)