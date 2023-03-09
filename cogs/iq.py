import discord
from discord.ext import commands
import random

class iq(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def iq(self, ctx,):
    embed = discord.Embed(description=f"`🥸` Your iq is `{random.randint(1, 251)}`.", color=0x2f3136)
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(iq(client))