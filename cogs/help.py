import discord
from discord.ext import commands
from datetime import datetime

# Load global config
config_file = open("configuration.yaml", "r")
config = yaml.safe_load(config_file)
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Ping the bot.")
    async def ping(self, ctx):
        await ctx.reply("Pong!", mention_author=False)
    
    @commands.command(brief="Leave a guild.")
    @commands.is_owner()
    async def leave_guild(self, ctx, id: str):
        await ctx.reply("Pong!", mention_author=False)
        

def setup(bot): 
    bot.add_cog(Help(bot))