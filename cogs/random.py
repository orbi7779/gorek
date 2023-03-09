import discord
from discord.ext import commands
import random

class rd(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def random(self, ctx):
    embed = discord.Embed(description=f":1234: Your random number is `{random.randrange(101)}`.", color=0x2f3136)
    await ctx.reply(embed=embed, mention_author=False)
    

async def setup(client):
  await client.add_cog(rd(client))