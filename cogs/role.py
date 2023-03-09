import discord
from discord.ext import commands

class role(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["ar"])
  @commands.has_permissions(manage_roles=True)
  async def addrole(self, ctx, user: discord.Member, *, role: discord.Role):
        if role in user.roles:
            embed = discord.Embed(title="", description=f"{user.mention} already has the role: **{role}**.", color=0x2f3136)
            await ctx.send(embed=embed)
        else:
            await user.add_roles(role)
            embed = discord.Embed(title="", description=f"Added **{role}** to {user.mention}.", color=0x2f3136)
            await ctx.reply(embed=embed, mention_author=False)

  @commands.command(aliases=["rr"])
  @commands.has_permissions(manage_roles=True)
  async def removerole(self, ctx, user: discord.Member, *, role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            embed = discord.Embed(title="", description=f"Removed **{role}** from {user.mention}.", color=0x2f3136)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="", description=f"{user.mention} does not have the role: **{role}**.", color=0x2f3136)
            await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(role(client))