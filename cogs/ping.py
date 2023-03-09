import discord
from discord.ext import commands

class ping(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    embed = discord.Embed(description=f"`🏓` Ping: `{round(self.client.latency * 1000)}ms`.", color=0x2f3136)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(ping(client))