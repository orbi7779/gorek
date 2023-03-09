from asyncio.tasks import wait
import discord
from discord.ext import commands
from discord import permissions
import os
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix=['.', ',', '<@1015589431173980252> '],
                      intents=intents)

client.remove_command('help')


@client.event
async def setup_hook():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(description="<:box:1071805357615231116> You didn't provide an argument.", color=0x2f3136)
    await ctx.send(embed=embed)
  elif isinstance(error, commands.CommandNotFound):
    embed = discord.Embed(description="<:h_:1071805355933306981> Command not found.", color=0x2f3136)
    await ctx.send(embed=embed)
  elif isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(description="<:i_:1071805353454489701> You do not have permission to use this command.", color=0x2f3136)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
  print(f"Jestem Gotowy do Pracy! Zalogowano jako {client.user.name}")
  await client.change_presence(activity=discord.Game(name=".help"))


client.run("MTAxNTU4OTQzMTE3Mzk4MDI1Mg.Gk_uKA.h4VS_o0nXuftIdq_Eh5QeGC49ZBwh1z9b0bw6w")