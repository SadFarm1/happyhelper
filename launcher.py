import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = commands.Bot(command_prefix='^')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Loading cogs...')
    load_cogs()
    print('Done loading cogs')
    print('------')

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



def check_cog(cog):
    return os.path.isfile(f'cogs/{cog}.py')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    if(check_cog(extension)):
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded module "{extension}"')
    else:
        await ctx.send(f'Could not find module "{extension}"')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    if(check_cog(extension)):
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded module "{extension}"')
    else:
        await ctx.send(f'Could not find module "{extension}"')


@bot.command(aliases=['r'])
@commands.check_any(commands.is_owner(), commands.has_permissions(kick_members=True))
async def reload(ctx, extension):
    if(check_cog(extension)):
        wait_msg = await ctx.send(f'Reloading module: "{extension}"')
        url = f'http://209.141.54.217:3000/SadFarm/HappyHelper/raw/branch/master/cogs/{extension}.py'
        r = requests.get(url)
    
        if(r.content != b'Not found.\n'):
            open(f'./cogs/{extension}.py', 'wb').write(r.content)
            
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded module "{extension}"')
        
    else:  
        await ctx.send(f'Could not find module "{extension}"')


@bot.command()
@commands.is_owner()
async def download(ctx, extension):
    wait_msg = await ctx.send(f'Downloading module: "{extension}"')
    url = f'http://209.141.54.217:3000/SadFarm/HappyHelper/raw/branch/master/cogs/{extension}.py'
    r = requests.get(url)
    
    if(r.content != b'Not found.\n'):
        open(f'./cogs/{extension}.py', 'wb').write(r.content)
        await wait_msg.edit(content=f'Downloaded module "{extension}"')
    else:
        await wait_msg.edit(content=f'Could not find module "{extension}"')


@download.error
async def download_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify a module to download')
    if(isinstance(error, commands.NotOwner)):
        await ctx.send('You do not have permission to use this command')


def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv('DISCORD_KEY'))