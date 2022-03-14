import discord
from discord.ext import commands
import datetime
import time

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):

        time.sleep(2.5)
        now = datetime.date.today()
        day = now.strftime('%w')

        now = datetime.datetime.today()
        hour = int(now.strftime('%H'))



        #if int(hour) <= 12 or int(hour) >= 23 and int(day) != 6 and int(day) != 0:
        if True:
            embed = discord.Embed(
                    title = "Ticket Alert",
                    description = "Welcome, Due to higher than normal inquires our response times are drastically delayed while we work through the tickets, thanks for your patience and understanding!",
                    color = 0x004c8b
                )
                await channel.send(embed=embed)
        else:

            if ('presales' in str(channel)):

                embed = discord.Embed(
                    title = "Presale Alert",
                    description = "Thank you for opening a ticket! You have reached us after our regular business hours. Response times may be impacted. Please leave a detailed message so we can assist you as soon as possible! \n\nThank you! \nExpect a response at around 7 AM (PST)",
                    color = 0x004c8b
                )
                await channel.send(embed=embed)

            elif ('support' in str(channel)):
                
                embed = discord.Embed(
                    title = "Support Alert",
                    description = "Thank you for opening a ticket! You have reached us after our regular business hours. Response times may be impacted. Please try our self service commands and/or leave a detailed message so we can assist you as soon as possible! \n\nThank you! \nExpect a response at around 7 AM (PST)",
                    color = 0x004c8b
                )
                await channel.send(embed=embed)
        
        elif int(day) == 6 or int(day) == 0 :

            if ('presales' in str(channel)):

                embed = discord.Embed(
                    title = "Presale Alert",
                    description = "Thank you for opening a Presales ticket! You have reached us during our weekend hours. Response times may be impacted. Please leave a detailed message so we can assist you as soon as possible!  \n\nThank you! \nExpected response times between 7 AM - 9 PM (PST)",
                    color = 0x004c8b
                )
                await channel.send(embed=embed)

            elif ('support' in str(channel)):

                embed = discord.Embed(
                    title = "Support Alert",
                    description = "Thank you for opening a Support ticket! You have reached us during our weekend hours. Response times may be impacted. Please try our self service commands and/or Please leave a detailed message so we can assist you as soon as possible!   \n\nThank you! \nExpected response times between 7 AM - 9 PM (PST)",
                    color = 0x004c8b
                )
                await channel.send(embed=embed)
        





def setup(bot):
    bot.add_cog(Tickets(bot))


    