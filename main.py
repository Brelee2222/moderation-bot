from keep_alive import keep_alive
import discord
import os
import random
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import time
client = discord.Client()
intents = discord.Intents.default()


client = commands.Bot(command_prefix = '*-',case_insensitive=True,help_command=None,intents = intents) 

embed=discord.Embed(title="About This Bot", color=random.randint(0,16777215))
embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/RlybECC5CEp9Xh9r3SG4J0zTX5g78IgkjpsHsiBrhBs/%3Fsize%3D128/https/cdn.discordapp.com/avatars/479792413884547072/e55d181cd42cacd15feef0075fae9115.png?width=80&height=80')
embed.add_field(name='Owner', value='Brelee#6122', inline=False)
embed.add_field(name='Invite url', value='[Invite](https://discord.com/api/oauth2/authorize?client_id=788244560051568681&permissions=8&scope=bot)', inline=False)
preloadedembeds=[embed]
print()
print(embed)
def refreshhelp(embeds):
  
  
  with open('help_.txt', 'r') as f:
    category=list(f.read().split(';'))
    print(category)
    for i in category:
      print(i)
      
      categori=list(i.split(':'))
      print(categori)
      embed=discord.Embed(title=categori[0], color=random.randint(0,16777215))
      del(categori[0])
      print(categori)
      for i in list(categori[0].split('~')):
        embed.add_field(name=('Commands that use this format' + list(i.split('*'))[0]), value=list(i.split('*'))[1], inline=False)
      embeds.append(embed)
      print(embeds)
  return embeds

start_time = 0
  
@client.event
async def on_ready():
    global start_time
    print("bot is ready")
    start_time = time.time()
    

@client.command()
async def about(ctx):
  await ctx.send(embed=preloadedembeds[0])
@client.command()
async def help(ctx):
  embeds=[]
  refreshhelp(embeds)
  print('done')
  print(embeds)
  for i in embeds:
    await ctx.send(embed=i)
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
  
  try:
    await member.kick(reason=reason)
    embed=discord.Embed(title=str(member) + 'has been kicked from the server', description=('Reason:' + reason), color=random.randint(0,16777215))
    await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title='Something went wrong when attempting to kick' + str(member), color=random.randint(0,16777215))
    await ctx.send(embed=embed)
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
  
  try:
    await member.ban(reason=reason)
    embed=discord.Embed(title=str(member) + 'has been banned from the server', description=('Reason:' + reason), color=random.randint(0,16777215))
    await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title='Something went wrong when attempting to ban' + str(member), color=random.randint(0,16777215))
    await ctx.send(embed=embed)
@client.event
async def on_raw_message_delete(message):
  print('de')
  with open('snipe.txt', 'r') as f:
    messages = list(f.read().split(''))
  if len(messages) >= 100:
    del(messages[0])
  print(type(message), message)
  messages.append(str((message.cached_message.channel.id, message.cached_message.guild.id, message.cached_message.content, (message.cached_message.author.name + message.cached_message.author.discriminator), message.cached_message.author.avatar_url)))

  with open('snipe.txt', 'w') as f:
    print(len(messages))
    print('   '.join([str(e) for e in messages]))
    f.write((''.join([str(elem) for elem in messages])).replace('\u0029\u0028', '').replace('\u0028', '').replace('\u0029', ''))

@client.command()
async def snipe(ctx):
  messages = []
  print('bruh')
  
  with open('snipe.txt', 'r') as f:
    for message in list(f.read().split('')):
      print(message)
      message = list(message.split(', '))
      if int(message[0]) == ctx.channel.id and int(message[1]) == ctx.guild.id:
        embed=discord.Embed(title=message[3], color=random.randint(0,16777215))
        embed.set_thumbnail(url=message[4].replace("<Asset url='", 'https://cdn.discordapp.com').replace('>', ''))
        embed.add_field(name='Message', value=message[2], inline=False)
        await ctx.send(embed=embed)
@client.command()
async def user(ctx, member : discord.Member):
  embed=discord.Embed(title=member.name + '#' + member.discriminator, color=random.randint(0,16777215))
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name='Roles', value=', '.join([str(e.mention) for e in member.roles]), inline=False)
  embed.add_field(name='Date registered', value=member.created_at, inline=False)
  embed.add_field(name='Date joined', value=member.joined_at, inline=False)
  await ctx.send(embed=embed)
@client.command()
async def ping(ctx):
  await ctx.send(("I have a ping latency of " + str(round(client.latency * 1000)) + 'ms'))
@client.command()
async def uptime(ctx):
  
  await ctx.send(("I've been online for " + str(round(time.time() - start_time)) + ' seconds'))
      
      


keep_alive()
client.run(os.getenv("TOKEN"))