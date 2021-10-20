import discord
from discord.ext import commands
from discord.ext import tasks
import requests
import time

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stats_update.start()

    

    @tasks.loop(hours=3)
    async def stats_update(self):
        try:
            

            r = requests.get('http://95.216.241.36:24833/api/v2?apikey=180263823b594706a4979f826aa10252&cmd=get_libraries')
            result = r.json()
            result = result['response']['data']
            

            media_count = {
                '4K Movies': 0,
                '4K TV Shows': 0,
                'Movies': 0,
                'TV': 0,
                'Kids Movies': 0,
                'Kids TV Shows': 0,
                'Anime': 0,
                'Audiobooks': 0,
                'Foreign TV Shows' :0,
                'Foreign Movies' :0,

            }

            library_names = [library['section_name'] for library in result]



            media_count['4K Movies'] = int(result[library_names.index("Movies  (4K)")]['count'])
            media_count['4K TV Shows'] = int(result[library_names.index("TV Shows  (4K)")]['count'])
            media_count['Movies'] = int(result[library_names.index("Movies")]['count'])
            media_count['TV'] = int(result[library_names.index("TV Shows")]['count'])
            media_count['Kids Movies'] = int(result[library_names.index("Movies  (Kids)")]['count'])
            media_count['Kids TV Shows'] = int(result[library_names.index("TV Shows  (Kids)")]
            ['count'])
            media_count['Audiobooks'] = int(result[library_names.index("Audiobooks")]['parent_count'])


            library_names.remove("Movies  (4K)")
            library_names.remove("TV Shows  (4K)")
            library_names.remove("Movies")
            library_names.remove("TV Shows")
            library_names.remove("Movies  (Kids)")
            library_names.remove("TV Shows  (Kids)")
            library_names.remove("Audiobooks")


            for libary in library_names:
                if 'anime' in str(libary).lower():
                    media_count['Anime'] += int(result[library_names.index(libary)]['count'])

                if 'TV Shows (' in str(libary):
                    media_count['Foreign TV Shows'] += int(result[library_names.index(libary)]['count'])

                if 'Movies (' in str(libary):
                    media_count['Foreign Movies'] += int(result[library_names.index(libary)]['count'])

    
            channel_ids = {
                '4K Movies': 780144070369738752,
                '4K TV Shows': 790992159192776714,
                'Movies': 780144157322379284,
                'TV': 780144200485306389,
                'Kids Movies': 780144242483789865,
                'Kids TV Shows': 780144303330033674,
                'Anime': 780144361861414971,
                'Audiobooks': 780144440731107349,
                'Foreign Movies': 850161942177251378,
                'Foreign TV Shows': 850161884254830603,
            }


            for channel_name in channel_ids:
                
                disc_channel = self.bot.get_channel(channel_ids[channel_name])
                
                time.sleep(2)
                await discord.VoiceChannel.edit(disc_channel, name = f'{channel_name}: {media_count[channel_name]}')
                
                
                



            
            
            
        except Exception as e:

            Sadf = self.bot.get_user(453959267347595276)

            await Sadf.send('An Error Occurred! Check Logs.')
            await Sadf.send(e)
            await Sadf.send(media_count)

 
         




def setup(bot):
    bot.add_cog(Stats(bot))


    