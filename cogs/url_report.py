import discord
import json

from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext

with open('ricks.json') as f:
    ricksData = json.load(f)

class ReportCog(Cog):
    @commands.command(aliases=['ur', 'report', 'urladd', 'add'])
    async def urlreport(self, ctx: MyContext, *, url):
        """
        Report a new url to Salvator
        """
        with open('ricks.json') as f:
            ricksData = json.load(f)
        ricksData.append(url)
        with open('ricks.json', 'w') as outfile:
            json.dump(ricksData, outfile)
        await ctx.send(f'URL <{url}> added to list of Rick-Roll URLs')

setup = ReportCog.setup
