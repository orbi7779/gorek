import discord
from discord.ext import commands
from discord.ui import Button, View

class wiki(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["wikipedia"])
  async def wiki(self, ctx, *, msg):
      msg = msg.replace(" ", "_")
      await ctx.reply(f"https://pl.wikipedia.org/wiki/{msg}", mention_author=False)

async def setup(client):
  await client.add_cog(wiki(client))