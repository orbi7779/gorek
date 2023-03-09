import discord
from discord.ext import commands

class h(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.group(name="help", invoke_without_command=True, aliases=["h"])
  async def help(self, ctx):
   embed = discord.Embed(
    title="Help",
    description=
    f"To see information about a command, type `.help <cmd>`. \n`< >` - This means the argument is required. \n`[ ]` - This means the argument is optional.",
    color=0x2f3136)
   embed.add_field(name="Bot:", value="```help, botinfo, complaint, opinion, invite,```")
   embed.add_field(name="Another:",
                  value="```serverinfo, userinfo, ping, avatar, membercount,```",
                  inline=False)
   embed.add_field(name="Fun:", value="```8ball, iq, coin, howgay, howcool, random, wiki, google, kiss, slap, tickle, hug, cat, dog, lizard,```", inline=False)
   embed.add_field(name="Moderation:", value="```ban, kick, clear, addrole, removerole, reaction, embed, question,```", inline=False)
   embed.add_field(name="Developer:", value="```reload,```")
   await ctx.reply(embed=embed, mention_author=False)

  @help.command(aliases=["help-test"])
  async def test(self, ctx):
    embed = discord.Embed(title="Help: test", description=f"Test. \n\n**How to use:** \n```.test``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-ban"])
  async def ban(self, ctx):
    embed = discord.Embed(title="Help: ban", description=f"Bans the user. \n\n**How to use:** \n```.ban <user> [reason]``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-kick"])
  async def kick(self, ctx):
    embed = discord.Embed(title="Help: kick", description=f"Kicks the user. \n\n**How to use:** \n```.kick <user> [reason]``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-iq"])
  async def iq(self, ctx):
    embed = discord.Embed(title="Help: iq", description=f"The bot tells you how much iq you have. \n\n**How to use:** \n```.iq``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-coin"])
  async def coin(self, ctx):
    embed = discord.Embed(title="Help: coin", description=f"The bot flips a coin. \n\n**How to use:** \n```.coin``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-ping"])
  async def ping(self, ctx):
    embed = discord.Embed(title="Help: ping", description=f"The bot shows you information about the ping. \n\n**How to use:** \n```.ping``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-serverinfo", "help-si"])
  async def serverinfo(self, ctx):
    embed = discord.Embed(title="Help: serverinfo", description=f"The bot shows you information about the server. \n\n**How to use:** \n```.serverinfo``` \n**Aliases:** \n```.si```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-botinfo", "help-bi"])
  async def botinfo(self, ctx):
    embed = discord.Embed(title="Help: botinfo", description=f"The bot shows you information about the bot. \n\n**How to use:** \n```.botinfo``` \n**Aliases:** \n```.bi```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-userinfo", "help-ui"])
  async def userinfo(self, ctx):
    embed = discord.Embed(title="Help: userinfo", description=f"The bot shows you information about the user. \n\n**How to use:** \n```.userinfo [user]``` \n**Aliases:** \n```.ui```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-avatar"])
  async def avatar(self, ctx):
    embed = discord.Embed(title="Help: avatar", description=f"The bot sends the user's avatar. \n\n**How to use:** \n```.avatar [user]``` \n**Aliases:** \n```.av```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-clear"])
  async def clear(self, ctx):
    embed = discord.Embed(title="Help: clear", description=f"The bot deletes messages. \n\n**How to use:** \n```.clear <amount>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-addrole", "help-ar"])
  async def addrole(self, ctx):
    embed = discord.Embed(title="Help: addrole", description=f"The bot gives the user a role. \n\n**How to use:** \n```.addrole <user> <role>``` \n**Aliases:** \n```.ar```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-removerole", "help-rr"])
  async def removerole(self, ctx):
    embed = discord.Embed(title="Help: removerole", description=f"The bot remove the user a role. \n\n**How to use:** \n```.removerole <user> <role>``` \n**Aliases:** \n```.rr```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["react"])
  async def reaction(self, ctx):
    embed = discord.Embed(title="Help: reaction", description=f"The bot adds an emoji to the message. \n\n**How to use:** \n```.reaction <msg id> <emoji>``` \n**Aliases:** \n```.react```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-question"])
  async def question(self, ctx):
    embed = discord.Embed(title="Help: question", description=f"The bot creates a question for the community. \n\n**How to use:** \n```.question <channel> <description>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-embed"])
  async def embed(self, ctx):
    embed = discord.Embed(title="Help: embed", description=f"The bot creates an embed. \n\n**How to use:** \n```.embed <channel> <title> <description>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-wiki"])
  async def wiki(self, ctx):
    embed = discord.Embed(title="Help: wiki", description=f"The bot searches for the given information on the wiki. \n\n**How to use:** \n```.wiki <text>``` \n**Aliases:** \n```.wikipedia```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-google"])
  async def google(self, ctx):
    embed = discord.Embed(title="Help: google", description=f"The bot searches for the given information on the google. \n\n**How to use:** \n```.google <text>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-kiss"])
  async def kiss(self, ctx):
    embed = discord.Embed(title="Help: kiss", description=f"You interact with the user and kiss him. \n\n**How to use:** \n```.kiss <user>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-hug"])
  async def hug(self, ctx):
    embed = discord.Embed(title="Help: hug", description=f"You interact with the user and give him a hug. \n\n**How to use:** \n```.hug <user>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-slap"])
  async def slap(self, ctx):
    embed = discord.Embed(title="Help: slap", description=f"You interact with the user and hit him. \n\n**How to use:** \n```.slap <user>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-tickle"])
  async def tickle(self, ctx):
    embed = discord.Embed(title="Help: tickle", description=f"You interact with the user and tickle them. \n\n**How to use:** \n```.tickle <user>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-cat"])
  async def cat(self, ctx):
    embed = discord.Embed(title="Help: cat", description=f"Bot send a random picture of a cat. \n\n**How to use:** \n```.cat``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-dog"])
  async def dog(self, ctx):
    embed = discord.Embed(title="Help: dog", description=f"Bot send a random picture of a dog. \n\n**How to use:** \n```.dog``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-lizard"])
  async def lizard(self, ctx):
    embed = discord.Embed(title="Help: lizard", description=f"Bot send a random picture of a lizard. \n\n**How to use:** \n```.lizard``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-complaint"])
  async def complaint(self, ctx):
    embed = discord.Embed(title="Help: complaint", description=f"With this command you can send a complaint to the board. \n\n**How to use:** \n```.complaint <description>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-opinion"])
  async def opinion(self, ctx):
    embed = discord.Embed(title="Help: opinion", description=f"You can send feedback to the board with this command. \n\n**How to use:** \n```.opinion <description>``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-invite"])
  async def invite(self, ctx):
    embed = discord.Embed(title="Help: invite", description=f"The bot sends its link to be added to the server. \n\n**How to use:** \n```.invite``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["r"])
  async def reload(self, ctx):
    embed = discord.Embed(title="Help: reload", description=f"A command that helps the *owner* reload files. \n\n**How to use:** \n```.reload <file>``` \n**Aliases:** \n```.r```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["gay"])
  async def howgay(self, ctx):
    embed = discord.Embed(title="Help: howgay", description=f"The bot shows you how gay you are. \n\n**How to use:** \n```.howgay``` \n**Aliases:** \n```.gay```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["cool"])
  async def howcool(self, ctx):
    embed = discord.Embed(title="Help: howcool", description=f"The bot shows you how cool you are. \n\n**How to use:** \n```.howcool``` \n**Aliases:** \n```.cool```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-random"])
  async def random(self, ctx):
    embed = discord.Embed(title="Help: random", description=f"The bot draws a number from 0 to 100. \n\n**How to use:** \n```.random``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["help-membercount"])
  async def membercount(self, ctx):
    embed = discord.Embed(title="Help: membercount", description=f"The bot shows how many people are on the server. \n\n**How to use:** \n```.membercount``` \n**Aliases:** \n```None```", color=0x2f3136)
    await ctx.send(embed=embed)

  @help.command(aliases=["8ball"])
  async def eightball(self, ctx):
    embed = discord.Embed(title="Help: 8ball", description=f"The bot answers your question. \n\n**How to use:** \n```.8ball <question>``` \n**Aliases:** \n```.8b```", color=0x2f3136)
    await ctx.send(embed=embed)

async def setup(client):
  await client.add_cog(h(client))