import discord
from discord.ext import commands

class embed(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def embed(self, ctx, channel: discord.TextChannel, name, *, des):
        embed = discord.Embed(title=f"{name}", description=f"{des}", color=0x2f3136)
        await channel.send(embed=embed)

async def setup(client):
  await client.add_cog(embed(client))