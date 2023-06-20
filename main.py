from datetime import datetime
import asyncio
import os
import random
import textwrap

import discord
from discord.ext import commands
from dotenv import load_dotenv

import neverSleep

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
            f"Welcome <@!{member.id}.>"
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

    if "1984" in message.content and message.author.id not in [
            801983327023398912, 1012755944846938163
    ]:
        await message.channel.send("literally 1984")

    # TODO: Move Kaczynski message command to messages.py
    if message.channel.id in [
            932896343901478963, 942683791753887804, 819110803612368896
    ] and message.author.id != 801983327023398912 and "c.kaczynski" not in message.content:
        with open("Resources/kaczynski_quotes.txt", "r") as f:
            content = f.read()
        content_list = content.split("\n\n")

        #choose random paragraph
        chosen_quote = random.choice(content_list)
        #separate footnotes
        footnote_split = chosen_quote.split("�")
        chosen_quote = footnote_split[0]
        footnote_split.pop(0)
        #split message if longer than 2000 characters and send
        split_quote = textwrap.wrap(chosen_quote, 2000)
        await message.channel.send(f"<@{message.author.id}>")
        for i in split_quote:
            await message.channel.send(i)
        #send footnotes and split them if too long
        for i in footnote_split:
            split_footnote = textwrap.wrap(i, 2000)
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


cog_list = [
    "acknowledgements",
    "cocanb",
    "messages",
    "misc",
    "moderation",
    "unicode",
    #"testing",
]


async def init_cogs():
    """ Initialize all cogs when the bot starts up """
    for cog in cog_list:
        await bot.load_extension(f"cogs.{cog}")


@bot.command()
async def reload(ctx):
    if ctx.author.id not in [607583934527569920, 448443875393273866]:
        await ctx.send("You do not have permissions to use this command")
        return

    msg = ""
    for cog in cog_list:
        try:
            await bot.reload_extension(f"cogs.{cog}")
            msg += f"Reloaded {cog}\n"
        except:
            msg += f"Failed to reload {cog}\n"
    await ctx.send(msg)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name='c.help'))

    await init_cogs()


try:
    bot.run(TOKEN)
except:
    os.system("kill 1")
