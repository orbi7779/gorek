import discord
from discord.ext import commands
from discord.ui import Button, View

class invite(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["i"])
  async def invite(self, ctx):
    button = Button(label="Invite Me", style=discord.ButtonStyle.link, url="https://discord.com/api/oauth2/authorize?client_id=1015589431173980252&permissions=8&scope=bot")
    view = View()
    view.add_item(button)
    embed = discord.Embed(description = "If you want, you can invite me to your server `:)`.", color=0x2f3136)

async def setup(client):
  await client.add_cog(invite(client))