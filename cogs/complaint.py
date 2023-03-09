import discord
from discord.ext import commands

class complaint(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def complaint(self, ctx, *, des):
      channel = self.client.get_channel(1068245525285048431)
      embed = discord.Embed(title="Complaint", description=f"{des}", color=0x2f3136)
      embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
      await channel.send(embed=embed)

async def setup(client):
  await client.add_cog(complaint(client))