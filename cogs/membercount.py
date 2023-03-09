import discord
from discord.ext import commands

class mc(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def membercount(self, ctx):
    embed = discord.Embed(description=f"`👤` There are `{ctx.guild.member_count}` users on this server.", color=0x2f3136)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(mc(client))