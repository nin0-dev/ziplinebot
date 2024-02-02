import discord
from discord.ext import commands
import yaml
import os
import cogs
from util import log, LogType, embed, EmbedType

# Load global config
try:
    config_file = open("configuration.yaml", "r")
except:
    print("Make sure configuration.yaml exists.")
    exit(1)
config = yaml.safe_load(config_file)
# Make client
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=commands.when_mentioned_or(config["prefix"]), intents=intents, owner_id=config["bot_owner"])

@client.event
async def on_ready():
    log("Bot connected!")
    log("--------------")
    # Load cogs
    cogs_list = [
        "help"
    ]
    for cog in cogs_list:
        client.load_extension(f"cogs.{cog}")
        log(f"Loaded cog: {cog}")

# Preliminary checks
if config["discord_token"] == "YOUR-TOKEN-HERE":
    log("Make sure to specify a bot token in configuration.yaml before actually starting your bot.", LogType.ERROR)
    exit(1)
if config["bot_owner"] == 0000000:
    log("Make sure to specify a bot owner in configuration.yaml before actually starting your bot.", LogType.ERROR)
    exit(1)

# Error handling
@client.event
async def on_command_error(ctx, error: discord.DiscordException):
    await ctx.reply(embed=embed("An error occured", f"Here are the error details: \n```{str(error)}```", EmbedType.ERROR), mention_author=False)

client.run(config["discord_token"])