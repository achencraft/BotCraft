import os
from tokenize import Token
import discord
import structlog
from os.path import join, dirname
from dotenv import load_dotenv 
from discord.ext import commands

log = structlog.get_logger()
dotenv_path = join(dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    log.info('loading environment')
    load_dotenv(dotenv_path)

TOKEN = os.getenv('BOT_TOKEN')
BOT_PREFIX = os.getenv('BOT_PREFIX', 'BotCraft ')
BOT_NAME = os.getenv('BOT_NAME','BotCraft')


intents = discord.Intents()
intents.members=True
bot = commands.Bot(command_prefix=BOT_PREFIX,  case_insensitive=True,intents=intents)

@bot.event
async def on_member_join(mbr):
    print(bot.guilds)
    role=discord.utils.get(mbr.guild.roles, name=os.getenv('BOT_VISITEUR_ROLE'))
    await mbr.add_roles(role)



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot_log_message(f"{BOT_NAME} a démarré.")
    action = discord.Game("Je cherche des Bugs")
    await bot.change_presence(status=discord.Status.online, activity=action)



async def bot_log_message(*args, **kwargs):
    BOT_LOG_CHANNEL_ID = os.getenv('BOT_LOG_CHANNEL_ID')

    try:
        if BOT_LOG_CHANNEL_ID:
            BOT_LOG_CHANNEL_ID = int(BOT_LOG_CHANNEL_ID)
            bot_log_channel = discord.utils.get(bot.get_all_channels(), id=BOT_LOG_CHANNEL_ID)
            
            if bot_log_channel:
                await bot_log_channel.send(*args, **kwargs)
            else:
                log.warning(f'Could not find bot log channel with id {BOT_LOG_CHANNEL_ID}')
    except Exception as e:
        print('Could not post message to bot log channel')

'''    
if __name__ == "__main__":
    EXTENSIONS = [
        'extensions.admin',
        'extensions.help',
        'extensions.next',
        'extensions.stoplist',
        'extensions.utils',
    ]

    for extension in EXTENSIONS:
        bot.load_extension(extension)
'''

bot.run(TOKEN, bot=True, reconnect=True)
