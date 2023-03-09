import discord
from discord.ext import commands

class kick(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user: discord.Member, *, reason="None"):
    try:
      await user.kick(reason=reason)
      embed = discord.Embed(title="", description=f"**{user}** has ben kicked. \nReason = **{reason}**", color=0x2f3136)
      await ctx.send(embed=embed)
    except:
      embed = discord.Embed(title="", description="Error", color=0x2f3136)
      await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(kick(client))