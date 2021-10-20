import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        pingmsg = await ctx.send(f'Pong!')

        await pingmsg.edit(content=f'Pong! {round(self.bot.latency * 1000)} ms')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def staffhelp(self, ctx):
        embed = discord.Embed(title="Staff Help", description="Commands For Staff", color=0x00ff00)
        embed.add_field(name="To enable/disable automatic ticket responses:", value="^toggleresponse", inline=False)
        embed.add_field(name="To reload stats module:", value="^r stats", inline=False)
        embed.add_field(name="To check if the bot is up:", value="^ping", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utilities(bot))


