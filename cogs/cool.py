import discord
from discord.ext import commands
import random

class cool(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def cool(self, ctx):
    embed = discord.Embed(description=f"`😎` You are `{random.randrange(101)}%` cool.", color=0x2f3136)
    await ctx.reply(embed=embed, mention_author=False)
    

async def setup(client):
  await client.add_cog(cool(client))