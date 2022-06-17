import discord
from discord.ext import commands , tasks
from discord  import FFmpegPCMAudio
import youtube_dl
from youtube_dl import YoutubeDL
import random
from random import choice
import DiscordUtils
import praw
from music_cog import music_cog
import asyncio
from ffmpeg import video

YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist':'True'}
FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': 'vn'}
reddit = praw.Reddit(client_id = 'uALiD6T8HzsGl6CWUw4SaA',
                                 client_secret = 'HM8Q6PuZ9QipML7t_ZSTIUHv-JgMHg',
                                 username = 'Impossible_Sky630',
                                 password = 'sourish1231',
                                 user_agent = 'discordmemes')
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '>',intents=intents)

client.add_cog(music_cog(client))

async def change_presence():
    await client.wait_until_ready()

    statuses = ["on Toastycraft", "on Whatsapp with the Friends", "with Lakshith's Memes","Minecraft" ]
    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)

@client.event
async def on_ready(pass_context = True):
    print("The BOT ISSSSSSSSSSSSSSSSSSSS READY")



@client.command()
async def hello(ctx):
    await ctx.send("Hello I will help you (kill)" +ctx.message.author.mention)

@client.event
async def on_member_join(member):
    channel = client.get_channel(981213955882123304)
    await channel.send(f"Hello! {member.mention}, Welcome to the Server!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(981213955882123304)
    await channel.send(f"Bye! {member.mention}, We Will Miss You!!")






@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    new = subreddit.new(limit=50)

    for submission in new:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)

    await ctx.send(embed= em)


@client.command()
async def linuxmeme(ctx):
    subreddit = reddit.subreddit("linuxmemes")
    all_subs = []
    new = subreddit.new(limit=50)

    for submission in new:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)

    await ctx.send(embed= em)

@client.command()
async def gamememe(ctx):
    subreddit = reddit.subreddit("gamingmemes")
    all_subs = []
    new = subreddit.new(limit=50)

    for submission in new:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)

    await ctx.send(embed= em)

@client.command()
async def genzmeme(ctx):
    subreddit = reddit.subreddit("GenZMemes")
    all_subs = []
    new = subreddit.new(limit=50)

    for submission in new:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)

    await ctx.send(embed= em)


client.loop.create_task(change_presence())
client.run("OTg3MDE2MDY1NzE4NTc5MjIw.G_qbTG.HrBD8CGzshdeIEuu1RloAMwKK6u1XaL0e5auEs")