import discord
from discord.ext import commands

class ban(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user: discord.Member, *, reason="None"):
    try:
      await user.ban(reason=reason)
      embed = discord.Embed(title="", description=f"**{user}** has ben banned. \nReason = **{reason}**", color=0x2f3136)
      await ctx.send(embed=embed)
    except:
      embed = discord.Embed(title="", description="Error", color=0x2f3136)
      await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(ban(client))