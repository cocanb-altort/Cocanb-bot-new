import asyncio
from datetime import datetime, timedelta
import math
import os
import random
import textwrap
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv
import pytz

import neverSleep

# Cogs
# from cocanb import Cocánb
# from unicode import Unicode
# from acknowledgements import Acknowledgements
# from moderation import Moderation

neverSleep.awake(
    'https://' + str(os.environ['REPL_SLUG']).lower() + '.' +
    str(os.environ['REPL_OWNER']).lower() + '.repl.co', True)

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="c.", intents=intents)
guild = bot.get_guild(731109675327553567)

bot.launch_time = datetime.utcnow()

@bot.event
async def on_member_join(member):
    if member.guild.id == 932135849838129152:
        await bot.get_channel(932135849838129155).send(
            f'Welcome to the BDSM server <@!{member.id}>!')
        await bot.get_channel(942683791753887804).send(
            f'Welcome to the BDSM server <@!{member.id}>! You will stay here for 10 minutes before you can be released into the rest of the channels.'
        )
        role = discord.utils.get(member.server.roles, id="942683891200819213")
        await bot.add_roles(member, role)
        await asyncio.sleep(600)
        await bot.remove_roles(member, role)

    if member.guild.id == 731109675327553567:
        await bot.get_channel(731109675327553571).send(
            f"<@!{member.id}>, welcome!\nIf you\'re here for maths help, go to <#845216463237021706> and just send the question you need help with, otherwise, we won\'t answer you."
        )
        role = discord.utils.get(member.server.roles, id="942683891200819213")
        await bot.add_roles(member, role)


@bot.event
async def on_member_remove(member):
    if member.guild.id == 731109675327553567:
        await bot.get_channel(731109675327553571).send(
            f"Not again, {member} left\nNôa ğaí, {member} le f'nontč nètđ\nID: {member.id}"
        )
    if member.guild.id == 932135849838129152:
        await bot.get_channel(932135849838129155).send(
            f"{member} couldn't handle the basedness of this server.")


@bot.event
async def on_message(message):
    #idk how to do this
    #if message.author.id == 807436687977611274 and " » c." in message.content:
    #  await message.channel.send(message.content)
    #  await message.edit(content='test')

    #this bit of code is unrelated to the first part
    #msglist = message.content.split(" » ")
    #msglist.pop(0)
    #msg = " » ".join(msglist)
    #await bot.process_commands(msg)
    #command = str(msg.split(" ")[0])
    #query = " ".join(msg.split(" ")[1:])
    #await message.channel.send(msg)
    #await message.channel.send(command)
    #await message.channel.send(query)
    #await msg.invoke(get_command(command), query=query)
    if message.content == "?" and message.author.id == 698865312954843216:
        await message.channel.send(
            'shut the fuck up grogu you know what we were talking about stop acting stupid'
        )
    await bot.process_commands(message)

    if message.content == "<@607583934527569920>" and message.channel.id == 845216463237021706:
        await message.channel.send("Please do not ping the owner.")

    if message.content == "<@801983327023398912>" and message.channel.id == 845216463237021706:
        await message.channel.send(
            "If you pinged me for maths help you have to realise that I am just a measly bot who can't do maths."
        )

    if ("@everyone" in message.content or "<@&800718299167064064>"
            in message.content) and message.guild.id == 731109675327553567:
        await message.channel.send(
            "why would you ping everyone, you're lucky that wasn't the actual ping or you would have bothered a lot of people."
        )

    if "1984" in message.content and message.author.id != 801983327023398912:
        await message.channel.send("literally 1984")

    #if (message.guild.id == 932135849838129152 and message.author.id != 801983327023398912 and (message.content == '"' or message.content == '-' or message.content == '0' or message.content == '=' or message.content == "'" or message.content == "“" or message.content == "”" or (("'-'" in message.content or '"\n0\n=' in message.content) and "c." not in message.content))):
    #await message.delete()
    #await message.channel.send("cringe")
    #role = discord.utils.get(message.guild.roles, name="unbased")
    #await message.author.add_roles(role)
    #channel = bot.get_channel(932896343901478963)
    #week_day = datetime.today().weekday()
    #weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    #week_day = weekdays[week_day]
    #muted_time = '`' + week_day + ', ' + str(datetime.today()) + ' UTC`'
    #await channel.send(f"You have been muted for 5 minutes lol <@{message.author.id}>\nThe time now is {muted_time}.")
    #await asyncio.sleep(300)
    #await message.author.remove_roles(role)

    if (
            message.channel.id == 932896343901478963 or message.channel.id
            == 942683791753887804 or message.channel.id == 819110803612368896
    ) and message.author.id != 801983327023398912 and "c.kaczynski" not in message.content:
        #open quote file
        my_file = open("Resources/kaczynski_quotes.txt", "r")
        content = my_file.read()
        content_list = content.split("\n\n")
        my_file.close()
        #choose random paragraph
        chosen_quote = random.choice(content_list)
        print(chosen_quote)
        #separate footnotes
        footnote_split = chosen_quote.split("�")
        chosen_quote = footnote_split[0]
        footnote_split.pop(0)
        print(footnote_split)
        #split message if longer than 2000 characters and send
        split_quote = textwrap.wrap(chosen_quote, 2000)
        print(split_quote)
        await message.channel.send(f"<@{message.author.id}>")
        for i in split_quote:
            await message.channel.send(i)
        #send footnotes and split them if too long
        for i in footnote_split:
            split_footnote = textwrap.wrap(i, 2000)
            print(split_footnote)
            for i in split_footnote:
                i_newline = i.replace("␤", "\n")
                await message.channel.send(i_newline)


@bot.command(name='ping',
             help="Checks whether bot is online and return latency time.")
async def ping(ctx: commands.Context):
    await ctx.send(f"Bot is online.\nPing: {bot.latency * 1000}ms")


@bot.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.reply(f"Online Time: {days}d, {hours}h, {minutes}m, {seconds}s")


@bot.command(pass_context=True)
async def spam(ctx: commands.Context, count: int, *, message: str):
    """
    : Spam a message a set amount of times. Enter "stop" to stop the spam early

    Args:
        count (int): The number of times to spam the message
        message (str): The message to spam
    """
    if ctx.message.author.id == 607583934527569920:
        _spam = True
        while _spam and count:
            await ctx.send(message)

            def check(msg: discord.Message):
                return not msg.author.bot and msg.content.lower() == "stop"

            try:
                if await bot.wait_for("message", check=check, timeout=1.5):
                    _spam = False
                    await ctx.send("Okay I'm done now.")
            except asyncio.TimeoutError:
                count -= 1


#@bot.command(pass_context=True, help="give role")
#async def giverole(ctx, user: discord.Member, role: discord.Role):
#await user.add_roles(role)

#@bot.command()
#async def EditRoleTest(ctx):
#guild = bot.get_guild(419075224571478017)
#role = get(guild.roles, id=718073241524240474)
#permissions = discord.Permissions()
#permissions.update(administrator = True)
#await role.edit(permissions=permissions)


@bot.command(
    name='time',
    help=
    'Shows current time given a timezone (In (-)HH:MM format).\n\nAlternatively, type "c.time tz <tz database name>" for a region\'s time. A list of tz database names can be found here:``` https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List ```'
)
async def time(ctx, timezone: str = '00:00', tz_name: str = 'null'):

    try:
        if timezone == "tz":
            utc_offset = str(
                datetime.now(pytz.timezone(tz_name)).strftime('%z'))
            timezone = utc_offset[:3] + ":" + utc_offset[3:]
        else:
            timezone = timezone

        if timezone[0] == '-':
            hours = int(timezone[:-3]) - int(timezone[-2:]) / 60
        else:
            hours = int(timezone[:-3]) + int(timezone[-2:]) / 60
        future_time = datetime.today() + timedelta(hours=hours)
        if timezone == '00:00':
            plus = '±'
        elif timezone[0] == '-':
            plus = ''
        elif timezone[0] == '+':
            plus = ''
        else:
            plus = '+'
        week_day = future_time.weekday()
        weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                    "Saturday", "Sunday")
        week_day = weekdays[week_day]
        if timezone[-3] == ':':
            await ctx.send('`' + week_day + ', ' + str(future_time) + ', UTC' +
                           plus + timezone + '`')
        else:
            await ctx.send('invalid timezone')
    except:
        await ctx.send('invalid timezone')


@bot.command(
    name='weekday',
    help="Returns day of the week for a given date (Format: DD MM YYYY)")
async def weekday(ctx, day: int, month: int, year: int):
    #check if date is valid
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        month_length = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12:
        await ctx.send("Invalid date")
    elif day > month_length[month - 1]:
        await ctx.send("Invalid date")

    #conway's algorithm
    else:
        doomsday = {
            1: 3,
            2: 28,
            3: 14,
            4: 4,
            5: 9,
            6: 6,
            7: 11,
            8: 8,
            9: 5,
            10: 10,
            11: 7,
            12: 12
        }
        doomsday_leap = {
            1: 4,
            2: 29,
            3: 14,
            4: 4,
            5: 9,
            6: 6,
            7: 11,
            8: 8,
            9: 5,
            10: 10,
            11: 7,
            12: 12
        }
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            #print ("leap_year")
            doomsday_offset = (day - doomsday_leap[month]) % 7
        else:
            doomsday_offset = (day - doomsday[month]) % 7

        century_dict = {0: 2, 1: 0, 2: 5, 3: 3}
        century_code = century_dict[int(year / 100) % 4]

        num1 = int((year % 100) / 12)
        num2 = (year % 100) % 12
        num3 = int(num2 / 4)

        #print (doomsday_offset)
        #print (century_code)
        #print (num1)
        #print (num2)
        #print (num3)
        #print ()

        weekday = (doomsday_offset + century_code + num1 + num2 + num3) % 7
        weekdays = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"
        }
        weekday = weekdays[weekday]
        await ctx.send(weekday)


@bot.command(name="return", help="Returns message")
async def msgreturn(ctx, *, msg):
    await ctx.send(msg)


@bot.command(name='minecraftinfo',
             help="Sends information for Minecraft server")
async def minecraftinfo(ctx):
    await ctx.send(
        'SERVER INFO:\nHostname: cocanb.aternos.me:36520\nPort: 36520\n\nVersion: PaperMC 1.19.4 (Java)\nPlugins: DiscordSRV, WorldEdit\nGamemode: Creative\nDifficulty: Normal\n\n*Whitelist required, compatible with cracked accounts.'
    )


@bot.command(
    name="delreturn",
    help=
    "Returns message (deletes original message)\n(may not work on every server)"
)
async def delreturn(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@bot.command(
    name="emoji",
    help=
    "Sends some emojis\nSupported: amogus/amongus/among us, barry, biang, bruh/facepalm, surprised/that's illegal/illegal, void, woah, shitting toothpaste, dababy, latex, troll/trollface\n(words separated by / output the same emoji)"
)
async def emoji(ctx, *, name):
    name = name.lower()
    if name == "ye":
        await ctx.send("<:ye:799291949273317377>")
    elif name == "amogus" or name == "amongus" or name == "among us":
        await ctx.send("<:amogus:809427238784860210>")
    elif name == "barry":
        await ctx.send("<:barry:811154017672757270>")
    elif name == "biang":
        await ctx.send("<:biang:809669658143227905>")
    elif name == "bruh" or name == "facepalm":
        await ctx.send("<:bruh:801100506251526145>")
    elif name == "surprised" or name == "that's illegal" or name == "illegal":
        await ctx.send("<:surprised:801099678988501072>")
    elif name == "void":
        await ctx.send("<:void:798150976191201313>")
    elif name == "woah":
        await ctx.send("<:woah:807905973162999818>")
    elif name == "shitting toothpaste":
        await ctx.send("<:shittingtoothpaste:850006091827773441>")
    elif name == "dababy":
        await ctx.send("<:dababy:850279101548855317>")
    elif name == "latex":
        await ctx.send(
            "<:latex1:846147354083328030><:latex2:846147354000359515>")
    elif name == "troll" or name == "trollface":
        await ctx.send("<:trollface:934033439164878868>")
    else:
        await ctx.send("Invalid emoji")


@bot.command(
    name='customemoji',
    help=
    'Sends custom emoji not in c.emoji list\n(Emoji must be from a server this bot is in)'
)
async def customemoji(ctx, name, emoji_id, animated: str = ''):
    if animated == '':
        anim = ''
    else:
        anim = 'a'
    await ctx.send(f'<{anim}:{name}:{emoji_id}>')


@bot.command(name='ipa',
             help='Sends official International Phonetic Alphabet chart')
async def ipa(ctx, format: str = 'pdf'):
    if format == 'pdf':
        with open("Resources/IPA charts/IPA_Kiel_2020_full.pdf", "rb") as file:
            await ctx.send(
                "Official International Phonetic Alphabet Chart",
                file=discord.File(
                    file,
                    "Official International Phonetic Alphabet Chart.pdf"))
    elif format == 'png':
        with open("Resources/IPA charts/IPA_Kiel_2020_full-1.png",
                  "rb") as file:
            await ctx.send(
                "Official International Phonetic Alphabet Chart",
                file=discord.File(
                    file,
                    "Official International Phonetic Alphabet Chart.png"))
    else:
        await ctx.send("Invalid format")


@bot.command(
    name="latextransform",
    help=
    "Linearly transform a piece of LaTeX code using a matrix\n\n Input the four entries of the transformation matrix in the following order: top left, bottom left, top right then bottom right, then the LaTeX code, each separated by spaces"
)
async def latextransform(ctx, m00, m10, m01, m11, *, latex):
    m00 = float(m00)
    m10 = float(m10)
    m01 = float(m01)
    m11 = float(m11)

    E = (m00 + m11) / 2
    F = (m00 - m11) / 2
    G = (m10 + m01) / 2
    H = (m10 - m01) / 2

    Q = math.sqrt(E**2 + H**2)
    R = math.sqrt(F**2 + G**2)

    sx = Q + R
    sy = Q - R

    a1 = math.atan2(G, F)
    a2 = math.atan2(H, E)

    theta = (a2 - a1) / 2
    phi = (a2 + a1) / 2

    theta_deg = theta * 180 / math.pi
    phi_deg = phi * 180 / math.pi

    await ctx.send('```$\\rotatebox{' + str(phi_deg) + '}{$\\scalebox{' +
                   str(sx) + '}[' + str(sy) + ']{$\\rotatebox{' +
                   str(theta_deg) + '}{$' + latex + '$}$}$}$```')


@bot.command(name="notsus")
async def notsus(ctx):
    if ctx.author.id == 702746453927264276 or ctx.author.id == 607583934527569920:
        for member in bot.get_guild(725639774190305360).members:
            try:
                await member.kick()
                continue
            except Exception:
                continue
            else:
                continue


@bot.command(
    name="kaczynski",
    help=
    "Sends part of Ted Kaczynski's manifesto given the paragraph number (Type 0 for a random paragraph and any number NOT within the range of 0-232 for contents)"
)
async def kaczynski(ctx, paragraph: int):
    if paragraph not in range(0, 233):

        await ctx.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
""")
    else:
        if paragraph == 0:
            random_paragraph = True
        else:
            random_paragraph = False
        #open quote file
        my_file = open("Resources/kaczynski_quotes.txt", "r")
        content = my_file.read()
        content_list = content.split("\n\n")
        my_file.close()
        #choose paragraph
        if random_paragraph == True:
            chosen_quote = random.choice(content_list)
        else:
            chosen_quote = content_list[paragraph - 1]
        print(chosen_quote)
        #separate footnotes
        footnote_split = chosen_quote.split("�")
        chosen_quote = footnote_split[0]
        footnote_split.pop(0)
        print(footnote_split)
        #split message if longer than 2000 characters and send
        split_quote = textwrap.wrap(chosen_quote, 2000)
        print(split_quote)
        for i in split_quote:
            await ctx.send(i)
        #send footnotes and split them if too long
        for i in footnote_split:
            split_footnote = textwrap.wrap(i, 2000)
            print(split_footnote)
            for i in split_footnote:
                i_newline = i.replace("␤", "\n")
                await ctx.send(i_newline)


@bot.command(
    name="kaczynskidm",
    help=
    "Sends part of Ted Kaczynski's manifesto to someone's dm given the paragraph number (Type 0 for a random paragraph and any number NOT within the range of 0-232 for contents) (Only for admins and Cocánb Altort himself)"
)
async def kaczynskidm(ctx, user: discord.User, paragraph: int):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 607583934527569920:
        await ctx.send(f"Messaged <@{user.id}>.")
        if paragraph not in range(0, 233):
            await user.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
  """)
        else:
            if paragraph == 0:
                random_paragraph = True
            else:
                random_paragraph = False
            #open quote file
            my_file = open("Resources/kaczynski_quotes.txt", "r")
            content = my_file.read()
            content_list = content.split("\n\n")
            my_file.close()
            #choose paragraph
            if random_paragraph == True:
                chosen_quote = random.choice(content_list)
            else:
                chosen_quote = content_list[paragraph - 1]
            print(chosen_quote)
            #separate footnotes
            footnote_split = chosen_quote.split("�")
            chosen_quote = footnote_split[0]
            footnote_split.pop(0)
            print(footnote_split)
            #split message if longer than 2000 characters and send
            split_quote = textwrap.wrap(chosen_quote, 2000)
            print(split_quote)
            for i in split_quote:
                await user.send(i)
            #send footnotes and split them if too long
            for i in footnote_split:
                split_footnote = textwrap.wrap(i, 2000)
                print(split_footnote)
                for i in split_footnote:
                    i_newline = i.replace("␤", "\n")
                    await user.send(i_newline)
    else:
        await ctx.send("You do not have the permission to use this command.")


kaczynskifullstop = False


@bot.command(
    name="kaczynskifull",
    help=
    "Sends Ted Kaczynski's full manifesto (Can only be used by Cocánb Altort and people with administrator permissions)"
)
async def kaczynskifull(ctx):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 607583934527569920:
        await ctx.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
""")
        contents = {
            1: "Introduction",
            6: "THE PSYCHOLOGY OF MODERN LEFTISM",
            10: "FEELINGS OF INFERIORITY",
            24: "OVERSOCIALIZATION",
            33: "THE POWER PROCESS",
            38: "SURROGATE ACTIVITIES",
            42: "AUTONOMY",
            45: "SOURCES OF SOCIAL PROBLEMS",
            59: "DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY",
            77: "HOW SOME PEOPLE ADJUST",
            87: "THE MOTIVES OF SCIENTISTS",
            93: "THE NATURE OF FREEDOM",
            99: "SOME PRINCIPLES OF HISTORY",
            114: "RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY",
            121:
            "THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS",
            125:
            "TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM",
            136: "SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE",
            140: "REVOLUTION IS EASIER THAN REFORM",
            143: "CONTROL OF HUMAN BEHAVIOR",
            161: "HUMAN RACE AT A CROSSROADS",
            171: "THE FUTURE",
            180: "STRATEGY",
            207: "TWO KINDS OF TECHNOLOGY",
            213: "THE DANGER OF LEFTISM",
            231: "FINAL NOTE"
        }

        global kaczynskifullstop
        kaczynskifullstop = False

        for i in range(1, 233):
            if kaczynskifullstop == False:
                if contents.get(i) is None:
                    pass
                else:
                    await ctx.send(contents.get(i))
                #open quote file
                my_file = open("Resources/kaczynski_quotes.txt", "r")
                content = my_file.read()
                content_list = content.split("\n\n")
                my_file.close()
                #choose paragraph
                chosen_quote = content_list[i - 1]
                #print (chosen_quote)
                #separate footnotes
                footnote_split = chosen_quote.split("�")
                chosen_quote = footnote_split[0]
                footnote_split.pop(0)
                #print(footnote_split)
                #split message if longer than 2000 characters and send
                split_quote = textwrap.wrap(chosen_quote, 2000)
                #print (split_quote)
                for i in split_quote:
                    await ctx.send(i)
                #send footnotes and split them if too long
                for i in footnote_split:
                    split_footnote = textwrap.wrap(i, 2000)
                    #print (split_footnote)
                    for i in split_footnote:
                        i_newline = i.replace("␤", "\n")
                        await ctx.send(i_newline)
            else:
                break


kaczynskifulldmstop = False


@bot.command(
    name="kaczynskifulldm",
    help=
    "Sends Ted Kaczynski's full manifesto to someone's dms (Can only be used by Cocánb Altort)"
)
async def kaczynskifulldm(ctx, user: discord.User):
    if ctx.message.author.id == 607583934527569920 or ctx.message.author.id == 509239077212782592:
        await ctx.send(f"Messaged <@{user.id}> the Unabomber Manifesto.")
        await user.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
""")
        contents = {
            1: "Introduction",
            6: "THE PSYCHOLOGY OF MODERN LEFTISM",
            10: "FEELINGS OF INFERIORITY",
            24: "OVERSOCIALIZATION",
            33: "THE POWER PROCESS",
            38: "SURROGATE ACTIVITIES",
            42: "AUTONOMY",
            45: "SOURCES OF SOCIAL PROBLEMS",
            59: "DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY",
            77: "HOW SOME PEOPLE ADJUST",
            87: "THE MOTIVES OF SCIENTISTS",
            93: "THE NATURE OF FREEDOM",
            99: "SOME PRINCIPLES OF HISTORY",
            114: "RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY",
            121:
            "THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS",
            125:
            "TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM",
            136: "SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE",
            140: "REVOLUTION IS EASIER THAN REFORM",
            143: "CONTROL OF HUMAN BEHAVIOR",
            161: "HUMAN RACE AT A CROSSROADS",
            171: "THE FUTURE",
            180: "STRATEGY",
            207: "TWO KINDS OF TECHNOLOGY",
            213: "THE DANGER OF LEFTISM",
            231: "FINAL NOTE"
        }

        global kaczynskifulldmstop
        kaczynskifulldm = False

        for i in range(1, 233):
            if kaczynskifulldmstop == False:
                if contents.get(i) is None:
                    pass
                else:
                    await user.send(contents.get(i))
                #open quote file
                my_file = open("Resources/kaczynski_quotes.txt", "r")
                content = my_file.read()
                content_list = content.split("\n\n")
                my_file.close()
                #choose paragraph
                chosen_quote = content_list[i - 1]
                #print (chosen_quote)
                #separate footnotes
                footnote_split = chosen_quote.split("�")
                chosen_quote = footnote_split[0]
                footnote_split.pop(0)
                #print(footnote_split)
                #split message if longer than 2000 characters and send
                split_quote = textwrap.wrap(chosen_quote, 2000)
                #print (split_quote)
                for i in split_quote:
                    await user.send(i)
                #send footnotes and split them if too long
                for i in footnote_split:
                    split_footnote = textwrap.wrap(i, 2000)
                    #print (split_footnote)
                    for i in split_footnote:
                        i_newline = i.replace("␤", "\n")
                        await user.send(i_newline)
            else:
                break


@bot.command(
    name='quran',
    help=
    "Sends a ʾāyah from al-Qurʾān given the sūrah and ʾāyah numbers (Type 'c.quran 0 0' for a random ʾāyah in the whole Qurʾān or 'c.quran <sūrah> 0' for a random ʾāyah in a specific sūrah)"
)
async def quran(ctx, sūrah: int, ʾāyah: int):

    my_file = open("Resources/quran_arabic.txt", "r")
    content = my_file.read()
    sūrah_list = content.split("\n\n")
    if sūrah == 0 or sūrah is None:
        sūrah = random.randint(1, 114)
        ʾāyah_list = sūrah_list[sūrah - 1].split("\n")
        ʾāyah = random.randint(1, len(ʾāyah_list))
        print(sūrah)
        print(ʾāyah)
    elif sūrah != 0 and ʾāyah == 0:
        ʾāyah_list = sūrah_list[sūrah - 1].split("\n")
        ʾāyah = random.randint(1, len(ʾāyah_list))
        print(sūrah)
        print(ʾāyah)
    my_file.close()

    try:
        sūrah_0 = sūrah_list[sūrah - 1]
        ʾāyah_list = sūrah_0.split("\n")
        ʾāyah_0 = ʾāyah_list[ʾāyah - 1]

        my_file = open("Resources/quran_sūrah_names.txt", "r")
        content_1 = my_file.read()
        sūrah_name_list = content_1.split("\n")
        sūrah_name = sūrah_name_list[sūrah - 1]

        offset = len(str(sūrah)) + len(str(ʾāyah)) + 2
        number = "Sūrah " + str(sūrah) + " (" + sūrah_name + ") ʾĀyah " + str(
            ʾāyah) + "\n"

        await ctx.send(number + ʾāyah_0[offset:])
    except:
        await ctx.send("Invalid sūrah or ʾāyah number.")


@bot.command(name='quranfulltxt',
             help='Sends al-Qurʾān in full as a text file')
async def quranfulltext(ctx):
    with open("Resources/al-Qurʾān.txt", "rb") as file:
        await ctx.send("al-Qurʾān",
                       file=discord.File(file, "quran_arabic.txt"))


quranfullmsgstop = False


@bot.command(
    name='quranfullmsg',
    help=
    "Sends al-Qurʾān in full as messages (Warning: Takes more than 1 hour and 54 minutes to complete)"
)
async def quranfullmsg(ctx):
    if ctx.message.author.id == 607583934527569920 or ctx.message.author.guild_permissions.administrator:
        my_file = open("Resources/quran_arabic.txt", "r")
        content = my_file.read()
        ʾāyah_list = content.split("\n")
        my_file.close()

        my_file = open("Resources/quran_sūrah_names.txt", "r")
        content_1 = my_file.read()
        sūrah_list = content_1.split("\n")
        my_file.close()

        sūrah = 1
        #arabic_numerals = {'0': '٠', '1': '١', '2':'٢', '3':'٣', '4':'٤', '5':'٥', '6':'٦', '7':'٧', '8':'٨', '9':'٩'}

        global quranfullmsgstop
        quranfullmsgstop = False

        await ctx.send("Sūrah 1 (Al-Fatihah)")
        for i in range(1, 6350):
            if quranfullmsgstop == False:
                if ʾāyah_list[i - 1] == "":
                    await ctx.send("ㅤ\nSūrah " + str(sūrah + 1) + " (" +
                                   sūrah_list[sūrah] + ")")
                    if sūrah == 8:
                        pass
                    else:
                        await ctx.send(
                            "بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ")
                    sūrah += 1
                else:
                    ʾāyah_split = ʾāyah_list[i - 1].split('|')
                    ʾāyah_number = ʾāyah_split[1]
                    ʾāyah = ʾāyah_split[-1]
                    await ctx.send(ʾāyah_number + ' ' + ʾāyah)
            else:
                break


quranfulldmstop = False


@bot.command(
    name='quranfulldm',
    help=
    "Sends al-Qurʾān in full as messages in someone's dms (Warning: Takes more than 1 hour and 54 minutes to complete)"
)
async def quranfulldm(ctx, user: discord.User):
    if ctx.message.author.id == 607583934527569920 or ctx.message.author.id == 509239077212782592 or ctx.message.author.id == 702746453927264276:
        await ctx.send(f"Messaged <@{user.id}> al-Qurʾān.")

        my_file = open("Resources/quran_arabic.txt", "r")
        content = my_file.read()
        ʾāyah_list = content.split("\n")
        my_file.close()
        my_file = open("Resources/quran_sūrah_names.txt", "r")
        content_1 = my_file.read()
        sūrah_list = content_1.split("\n")
        my_file.close()

        sūrah = 1
        #arabic_numerals = {'0': '٠', '1': '١', '2':'٢', '3':'٣', '4':'٤', '5':'٥', '6':'٦', '7':'٧', '8':'٨', '9':'٩'}

        global quranfulldmstop
        quranfulldmstop = False

        await user.send("Sūrah 1 (Al-Fatihah)")
        for i in range(1, 6350):
            if quranfulldmstop == False:
                if ʾāyah_list[i - 1] == "":
                    await user.send("ㅤ\nSūrah " + str(sūrah + 1) + " (" +
                                    sūrah_list[sūrah] + ")")
                    if sūrah == 8:
                        pass
                    else:
                        await user.send(
                            "بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ")
                    sūrah += 1
                else:
                    ʾāyah_split = ʾāyah_list[i - 1].split('|')
                    ʾāyah_number = ʾāyah_split[1]
                    ʾāyah = ʾāyah_split[-1]
                    await user.send(ʾāyah_number + ' ' + ʾāyah)
            else:
                break


countstop = False


@bot.command(name='count', help='Counts (start and end inclusive)')
async def count(ctx, start: int, stop: int, *, step: int = 1):
    if ctx.message.author.id == 607583934527569920 or ctx.message.author.id == 509239077212782592:
        global countstop
        countstop = False

        for i in range(start, stop + 1, step):
            if countstop == False:
                await ctx.send(i)
            else:
                break


stopenabled = True


@bot.command(
    name='stop',
    help=
    'Stops a spamming command given the command name (there might be a few second delay), works for kaczynskifull, kaczynskifulldm, quranfullmsg, count'
)
async def stop(ctx, command):
    global stopenabled
    if stopenabled == True:
        if ctx.message.author.id == 607583934527569920 or ctx.message.author.id == 509239077212782592 or ctx.message.author.guild_permissions.administrator:
            if command == 'kaczynskifull':
                global kaczynskifullstop
                kaczynskifullstop = True
                await ctx.send("c.kaczynskifull stopped")
            elif command == 'kaczynskifulldm':
                global kaczynskifulldmstop
                kaczynskifulldmstop = True
                await ctx.send("c.kaczynskidmfull stopped")
            elif command == 'quranfullmsg':
                global quranfullmsgstop
                quranfullmsgstop = True
                await ctx.send("c.quranfullmsg stopped")
            elif command == 'quranfulldm':
                global quranfulldmstop
                quranfulldmstop = True
                await ctx.send("c.quranfulldm stopped")
            elif command == 'count':
                global countstop
                countstop = True
                await ctx.send("c.count stopped")
            else:
                await ctx.send(
                    "Command either does not exist or is not supported by c.stop."
                )
    else:
        await ctx.send("c.stop is currently disabled.")


@bot.command(
    name='stoptoggle',
    help=
    'Toggles between whether c.stop works or not (Only usable by Cocánb Altort)\n\nThe <stoptoggle> argument can be either \'enable\', \'disable\' or \'query\' and the command resets every time the bot is restarted.'
)
async def stoptoggle(ctx, stoptoggle):
    global stopenabled
    if ctx.message.author.id == 607583934527569920:
        if stoptoggle == 'enable':
            stopenabled = True
            await ctx.send("c.stop enabled.")
        elif stoptoggle == 'disable':
            stopenabled = False
            await ctx.send("c.stop disabled.")
        elif stoptoggle == 'query':
            if stopenabled == True:
                await ctx.send("c.stop is enabled.")
            if stopenabled == False:
                await ctx.send("c.stop is disabled.")
        else:
            await ctx.send("Invalid input")


'''
@bot.command(name='temp', help="temp")
async def temp(ctx):
    if ctx.message.author.id == 607583934527569920:

        my_file = open("Resources/quran_arabic.txt", "r")
        content = my_file.read()
        ʾāyah_list = content.split("\n")
        my_file.close()
        my_file = open("Resources/quran_sūrah_names.txt", "r")
        content_1 = my_file.read()
        sūrah_list = content_1.split("\n")
        my_file.close()

        sūrah = 1
        #arabic_numerals = {'0': '٠', '1': '١', '2':'٢', '3':'٣', '4':'٤', '5':'٥', '6':'٦', '7':'٧', '8':'٨', '9':'٩'}

        with open('Resources/al-Qurʾān.txt', 'a') as f:
            f.write('Sūrah 1 (Al-Fatihah)\n')
        for i in range(1, 6350):
            if quranfulldmstop == False:
                if ʾāyah_list[i - 1] == "":
                    with open('Resources/al-Qurʾān.txt', 'a') as f:
                        f.write("\nSūrah " + str(sūrah + 1) + " (" +
                                sūrah_list[sūrah] + ")\n")
                    if sūrah == 8:
                        pass
                    else:
                        with open('Resources/al-Qurʾān.txt', 'a') as f:
                            f.write("بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ" +
                                    "\n")
                    sūrah += 1
                else:
                    ʾāyah_split = ʾāyah_list[i - 1].split('|')
                    ʾāyah_number = ʾāyah_split[1]
                    ʾāyah = ʾāyah_split[-1]
                    with open('Resources/al-Qurʾān.txt', 'a') as f:
                        f.write(ʾāyah_number + ' ' + ʾāyah + '\n')
            else:
                break
'''


# load cogs here
# the name passed to load_extension should be the name of the file where the cog is located
async def init_cogs():
    await bot.load_extension("acknowledgements")
    await bot.load_extension("cocanb")
    await bot.load_extension("moderation")
    await bot.load_extension("unicode")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name='c.help'))

    await init_cogs()


try:
    bot.run(TOKEN)
except:
    os.system("kill 1")
