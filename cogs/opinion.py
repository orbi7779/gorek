import discord
from discord.ext import commands

class opinion(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def opinion(self, ctx, *, des):
      channel = self.client.get_channel(1068245525285048431)
      embed = discord.Embed(title="Opinion", description=f"{des}", color=0x2f3136)
      embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
      await channel.send(embed=embed)

async def setup(client):
  await client.add_cog(opinion(client))