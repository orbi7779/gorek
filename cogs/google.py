import discord
from discord.ext import commands
from discord.ui import Button, View


class google(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["search"])
  async def google(self, ctx, *, msg):
      msg = msg.replace(" ", "_")
      await ctx.reply(f"https://www.google.pl/search?q={msg}", mention_author=False)

async def setup(client):
  await client.add_cog(google(client))