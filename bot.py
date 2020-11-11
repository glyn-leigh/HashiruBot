import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client(command_prefix = '#')
discord = discord

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

bot.run(DISCORD_TOKEN)