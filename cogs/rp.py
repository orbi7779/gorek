import discord
from discord.ext import commands
import requests

class rp(commands.Cog):

  def __init__(self, client):
    self.client = client





  @commands.command()
  async def slap(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/slap")
    res = slapp.json()
    embed=discord.Embed(description=f"{ctx.author.mention} slapped {member.mention}.", color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)






  @commands.command()
  async def tickle(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/tickle")
    res = slapp.json()
    embed=discord.Embed(description=f"{ctx.author.mention} tickle {member.mention}.", color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)






  @commands.command()
  async def kiss(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/kiss")
    res = slapp.json()
    embed=discord.Embed(description=f"{ctx.author.mention} kisses {member.mention}.", color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)





  @commands.command()
  async def hug(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/hug")
    res = slapp.json()
    embed=discord.Embed(description=f"{ctx.author.mention} hugged {member.mention}.", color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)




  @commands.command()
  async def cat(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/meow")
    res = slapp.json()
    embed=discord.Embed(color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)




  @commands.command()
  async def dog(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/woof")
    res = slapp.json()
    embed=discord.Embed(color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)


  @commands.command()
  async def lizard(self, ctx, member: discord.Member=None):
    slapp = requests.get("https://nekos.life/api/v2/img/lizard")
    res = slapp.json()
    embed=discord.Embed(color=0x2f3136)
    embed.set_image(url=res["url"])
    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(rp(client))