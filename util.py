import colorama
from colorama import Fore, Style
import datetime
import enum
import discord

class LogType(enum.Enum):
    INFO = 0
    WARNING = -1
    ERROR = -2
def log(message: str, type: LogType = LogType.INFO):
    if type == LogType.INFO:
        print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now())} {Fore.LIGHTBLUE_EX}{Style.BRIGHT}INFO{Style.RESET_ALL}: {message}{Style.RESET_ALL}")
    if type == LogType.WARNING:
        print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now())} {Fore.YELLOW}{Style.BRIGHT}WARNING{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}: {message}{Style.RESET_ALL}")
    if type == LogType.ERROR:
        print(f"{Fore.LIGHTBLACK_EX}{str(datetime.datetime.now())} {Fore.RED}{Style.BRIGHT}ERROR{Style.RESET_ALL}{Fore.LIGHTRED_EX}: {message}{Style.RESET_ALL}")

class EmbedType(enum.Enum):
    INFO = 0
    SUCCESS = 1
    ERROR = -1
def embed(title: str, description: str, type: EmbedType = EmbedType.INFO):
    embed = discord.Embed()
    if type == EmbedType.SUCCESS:
        # Set color
        embed.color = 0x69FF7E
        # Set title
        embed.title = "✅ " + title
    if type == EmbedType.ERROR:
        # Set color
        embed.color = 0xFF6969
        # Set title
        embed.title = "❌ " + title
    else:
        # Set title
        embed.title = title
    # Set description
    embed.description = description
    return embed