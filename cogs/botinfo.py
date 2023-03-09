import discord
from discord.ext import commands
from discord.ui import Button, View

class bi(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["bi"])
  async def botinfo(self, ctx):
    embed = discord.Embed(
        title="Bot Info:",
        description=
        f"\n\n<:ping:1067419926647799829> **ping:** `{round(self.client.latency * 1000)}ms`,\n<:cash:1067419191013023764> **prefix:** `.`, `,`, `@gorek`, \n<:starsh:1067419197187035136> **commands:** `34`, \n <:pe:1070238244740014120> **bot:** `{len(self.client.users)}` users on `{len(self.client.guilds)}` servers,",
        color=0x2f3136)
    button = Button(label="Support", style=discord.ButtonStyle.link, url="https://discord.gg/37PHb9GEXe")
    view = View()
    view.add_item(button)
    await ctx.reply(embed=embed, mention_author=False, view=view)

async def setup(client):
  await client.add_cog(bi(client))