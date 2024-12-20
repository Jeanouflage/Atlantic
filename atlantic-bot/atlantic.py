import discord
from discord.ext import commands
import random

# Set up the bot with the necessary intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

async def on_message(message):
    if message.author == client.user:
        return

# Define a slash command (application command)
@bot.tree.command(name="hello", description="Say hello to Atlantic!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"woof woof, my name is Atlantic.. nice to meet you, <@{interaction.user.id}>")

@bot.tree.command(name="aboutme", description="About Atlantic.")
async def aboutme(interaction: discord.Interaction):
    await interaction.response.send_message(f"woof woof - my name is Atlantic, and i'm a dog. i like bones. go check out /commands to check out what i can do")

@bot.tree.command(name="commands", description="Atlantic's commands.")
async def commands(interaction: discord.Interaction):
    await interaction.response.send_message(f"My commands: /hello /aboutme /commands /goodvibes /roast /8ball")

@bot.tree.command(name="goodvibes", description="Get some good vibes.")
async def goodvibes(interaction: discord.Interaction):
    try:
        with open("goodvibes.txt", "r") as file:
            lines = file.readlines()
            if not lines:
              await interaction.response.send_message("Error: File is empty.")
              return
        randomLine = random.choice(lines).strip()
        await interaction.response.send_message(randomLine)
    except FileNotFoundError:
        await interaction.response.send_message("Error: File not found.")

@bot.tree.command(name="roast", description="Get roasted.")
async def roast(interaction: discord.Interaction):
    try:
        with open("roast.txt", "r") as file:
            lines = file.readlines()
            if not lines:
              await interaction.response.send_message("Error: File is empty.")
              return
        randomLine = random.choice(lines).strip()
        await interaction.response.send_message(randomLine)
    except FileNotFoundError:
        await interaction.response.send_message("Error: File not found.")

eightballList = ["yes" , "no"]
eightballRandom = random.choice(eightballList)

@bot.tree.command(name="8ball", description="Ask a question and Atlantic will answer yes or no.")
async def eightball(interaction: discord.Interaction, question: str = None):
    if not question:
        await interaction.response.send_message("where's your question???")
    eightballRandom = random.choice(eightballList)
    await interaction.response.send_message(eightballRandom)

@bot.tree.command(name="snowball", description="Throw a snowball at Atlantic.")
async def snowball(interaction: discord.Interaction):
    try:
        with open("snowball.txt", "r") as file:
            lines = file.readlines()
            if not lines:
              await interaction.response.send_message("Error: File is empty.")
              return
        randomLine = random.choice(lines).strip().replace("\\n", "\n")
        await interaction.response.send_message(randomLine)
    except FileNotFoundError:
        await interaction.response.send_message("Error: File not found.")
    
@bot.tree.command(name="happychristmas", description="Wish Atlantic a Happy Christmas.")
async def happychristmas(interaction: discord.Interaction):
    try:
        with open("happychristmas.txt", "r") as file:
            lines = file.readlines()
            if not lines:
              await interaction.response.send_message("Error: File is empty.")
              return
        randomLine = random.choice(lines).strip().replace("\\n", "\n")
        await interaction.response.send_message(randomLine)
    except FileNotFoundError:
        await interaction.response.send_message("Error: File not found.")

# Run the bot
@bot.event
async def on_ready():
    try:
        await bot.tree.sync()  # Sync the application commands
        print(f"Bot is up and running! (logged in as {bot.user})")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run("ur mum")
