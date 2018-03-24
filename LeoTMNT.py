# Leo by beatbox1200

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='L!')

@bot.event
async def on_ready():
    print ("Ready when you are!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged.")

@bot.command(pass_context=True)
async def favcolor(ctx):
    await bot.say("My favorite color is Blue, like my bandana!")
    print ("user has asked bot for favorite color.")

@bot.command(pass_context=True)
async def hey(ctx):
    await bot.say("Sup, bro!")
    print ("user has said hello to bot.")

@bot.command(pass_context=True)
async def bye(ctx):
    await bot.say("See you later, my man!")
    print ("user has said farwell to the bot.")

@bot.command(pass_context=True)
async def brothers(ctx):
    await bot.say("My brothers are Donnie, Raph, and Mikey. Anything else you want to know about my PERSONAL life?")
    print ("user has been burned by the bot after asking who its brothers were.")

@bot.command(pass_context=True)
async def favsongs(ctx):
    await bot.say("1. I Miss You - Clean Bandit ft. Julia Michaels. 2. Let Me Go - Hailee Steinfeld, Florida Georgia Line, and Alesso. 3. Heroes - Alesso. 4. It Aint Me - Kygo X Selena Gomez. 5. Faded - Alan Walker ft. Iselin Solheim")
    print ("user has asked bot favorite songs.")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Never come back, {}. Shredder Fan!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def say(ctx, *, something):
    await bot.say(something)

@bot.command(pass_context=True)
async def nickchange(ctx, user: discord.member):
    await bot.say ("Nickname of Member has been successfuly changed.")
    await bot.change_nickname(discord.member)

@bot.command(pass_context=True)
async def cmdsuggest(ctx, *, suggestion):
    await bot.send_message(discord.Object ("426122260697448474"), """
Username: {}
Rank: {}
Command Suggestion: {}""".format(ctx.message.author.name, ctx.message.author.top_role.name, suggestion)) 
    await bot.say("Your command suggestion has been recorded and was sent to an HR.")


@bot.command(pass_context=True)
async def respond1():
    await bot.say("Oh my god... Raph! How are you?")

@bot.event
async def on_message(msg):
    if msg.author.id == "426157101400850443" and msg.content == "It's been going really fine. Ever since I joined Beat's server, him and his friends have been helping me out with my anger. I really appreciate it! I hope to see you around!":
        await bot.send_message(msg.channel, "That's good. I decided not to be an information turtle. I just want to be a turtle with a free life just like the others. See you around!")    
    


bot.run(os.getenv(TOKEN))
