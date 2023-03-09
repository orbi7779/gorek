import discord
from discord.ext import commands

class ui(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["ui"])
  async def userinfo(self, ctx, user: discord.Member = None):

    if user == None:
        user = ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)

    embed = discord.Embed(title="User Info", color=0x2f3136)
    embed.set_thumbnail(url=user.avatar),
    embed.add_field(name="ID: ", value=user.id, inline=False)
    embed.add_field(name="Name: ", value=user.display_name, inline=False)
    embed.add_field(name="Created at: ",
                    value=user.created_at.__format__("%A, %d. %B %Y | %H:%M:%S"),
                    inline=False)
    embed.add_field(name="Joined at: ",
                    value=user.joined_at.__format__("%A, %d. %B %Y | %H:%M:%S"),
                    inline=False)
    embed.add_field(name="Bot?: ", value=user.bot, inline=False)
    embed.add_field(name=f"Roles ({len(rlist)}):", value="".join([b]), inline=False)
    embed.add_field(name=f"Top Role:", value=user.top_role.mention, inline=False)

    await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
  await client.add_cog(ui(client))