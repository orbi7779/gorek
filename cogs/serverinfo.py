import discord
from discord.ext import commands

class si(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["si"])
  async def serverinfo(self, ctx):
   owner = ctx.guild.owner_id
   
   embed = discord.Embed(title="Server Info", color=0x2f3136)

   embed.add_field(name="ID: ", value=ctx.guild.id, inline=False)
   embed.add_field(name="Name: ", value=ctx.guild.name, inline=False)
   embed.add_field(name="Server Owner: ", value=f"<@{owner}>", inline=False)
   embed.add_field(name="Text Channels: ",
                  value=len(ctx.message.guild.text_channels),
                  inline=False)
   embed.add_field(name="Voice Channels: ",
                  value=len(ctx.message.guild.voice_channels),
                  inline=False)
   embed.add_field(name="Roles: ",
                  value=len(ctx.message.guild.roles),
                  inline=False)
   embed.add_field(
    name="Created at: ",
    value=ctx.guild.created_at.__format__("%A, %d. %B %Y | %H:%M:%S"),
    inline=False)
   embed.set_thumbnail(url=f"{ctx.guild.icon}")

   await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(si(client))