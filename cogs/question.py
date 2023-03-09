import discord
from discord.ext import commands

class question(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def question(self, ctx, channel: discord.TextChannel, *, question):
        embed = discord.Embed(title="Question", description=f"{question}", color=0x2f3136)
        msg = await channel.send(embed=embed)
        await msg.add_reaction('<:yes:1070778893889450126>')
        await msg.add_reaction('<:idk:1070778892782153829>')
        await msg.add_reaction('<:no:1070778890278158386>')

async def setup(client):
  await client.add_cog(question(client))