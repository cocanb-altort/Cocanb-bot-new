import asyncio
import random
import textwrap

import discord
from discord.ext import commands


class Kaczynski:
    contents_str = """
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
"""

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


class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="return", help="Returns message")
    async def msgreturn(self, ctx, *, msg):
        await ctx.send(msg)

    @commands.command(
        name="delreturn",
        help=
        "Returns message (deletes original message)\n(may not work on every server)"
    )
    async def delreturn(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def spam(self, ctx: commands.Context, count: int, *, message: str):
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
                    if await self.bot.wait_for("message",
                                               check=check,
                                               timeout=1.5):
                        _spam = False
                        await ctx.send("Okay I'm done now.")
                except asyncio.TimeoutError:
                    count -= 1

    @commands.command(
        name="kaczynski",
        help=
        "Sends part of Ted Kaczynski's manifesto given the paragraph number (Type 0 for a random paragraph and any number NOT within the range of 0-232 for contents)"
    )
    async def kaczynski(self, ctx, paragraph: int):
        if paragraph not in range(0, 233):

            await ctx.send(Kaczynski.contents_str)
        else:
            if paragraph == 0:
                random_paragraph = True
            else:
                random_paragraph = False
            #open quote file
            with open("Resources/kaczynski_quotes.txt", "r") as f:
                content = f.read()
                content_list = content.split("\n\n")

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

    @commands.command(
        name="kaczynskidm",
        help=
        "Sends part of Ted Kaczynski's manifesto to someone's dm given the paragraph number (Type 0 for a random paragraph and any number NOT within the range of 0-232 for contents) (Only for admins and Cocánb Altort himself)"
    )
    async def kaczynskidm(self, ctx, user: discord.User, paragraph: int):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 607583934527569920:
            await ctx.send(f"Messaged <@{user.id}>.")
            if paragraph not in range(0, 233):
                await user.send(Kaczynski.contents_str)
            else:
                if paragraph == 0:
                    random_paragraph = True
                else:
                    random_paragraph = False
                #open quote file
                with open("Resources/kaczynski_quotes.txt", "r") as f:
                    content = f.read()
                    content_list = content.split("\n\n")

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
            await ctx.send(
                "You do not have the permission to use this command.")

    kaczynskifullstop = False

    @commands.command(
        name="kaczynskifull",
        help=
        "Sends Ted Kaczynski's full manifesto (Can only be used by Cocánb Altort and people with administrator permissions)"
    )
    async def kaczynskifull(self, ctx):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 607583934527569920:
            await ctx.send(Kaczynski.contents_str)

            global kaczynskifullstop
            kaczynskifullstop = False

            for i in range(1, 233):
                if kaczynskifullstop == False:
                    if Kaczynski.contents.get(i) is None:
                        pass
                    else:
                        await ctx.send(Kaczynski.contents.get(i))
                    #open quote file
                    with open("Resources/kaczynski_quotes.txt", "r") as f:
                        content = f.read()
                        content_list = content.split("\n\n")

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

    @commands.command(
        name="kaczynskifulldm",
        help=
        "Sends Ted Kaczynski's full manifesto to someone's dms (Can only be used by Cocánb Altort)"
    )
    async def kaczynskifulldm(self, ctx, user: discord.User):
        if ctx.message.author.id == 607583934527569920 or ctx.message.author.id == 509239077212782592:
            await ctx.send(f"Messaged <@{user.id}> the Unabomber Manifesto.")
            await user.send(Kaczynski.contents_str)

            global kaczynskifulldmstop
            kaczynskifulldm = False

            for i in range(1, 233):
                if kaczynskifulldmstop == False:
                    if Kaczynski.contents.get(i) is None:
                        pass
                    else:
                        await user.send(Kaczynski.contents.get(i))
                    #open quote file
                    with open("Resources/kaczynski_quotes.txt", "r") as f:
                        content = f.read()
                        content_list = content.split("\n\n")

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

    @commands.command(
        name='quran',
        help=
        "Sends a ʾāyah from al-Qurʾān given the sūrah and ʾāyah numbers (Type 'c.quran 0 0' for a random ʾāyah in the whole Qurʾān or 'c.quran <sūrah> 0' for a random ʾāyah in a specific sūrah)"
    )
    async def quran(self, ctx, sūrah: int, ʾāyah: int):

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
            number = "Sūrah " + str(
                sūrah) + " (" + sūrah_name + ") ʾĀyah " + str(ʾāyah) + "\n"

            await ctx.send(number + ʾāyah_0[offset:])
        except:
            await ctx.send("Invalid sūrah or ʾāyah number.")

    @commands.command(name='quranfulltxt',
                      help='Sends al-Qurʾān in full as a text file')
    async def quranfulltext(self, ctx):
        with open("Resources/al-Qurʾān.txt", "rb") as file:
            await ctx.send("al-Qurʾān",
                           file=discord.File(file, "quran_arabic.txt"))

    quranfullmsgstop = False

    @commands.command(
        name='quranfullmsg',
        help=
        "Sends al-Qurʾān in full as messages (Warning: Takes more than 1 hour and 54 minutes to complete)"
    )
    async def quranfullmsg(self, ctx):
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

    @commands.command(
        name='quranfulldm',
        help=
        "Sends al-Qurʾān in full as messages in someone's dms (Warning: Takes more than 1 hour and 54 minutes to complete)"
    )
    async def quranfulldm(self, ctx, user: discord.User):
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

    @commands.command(name='count', help='Counts (start and end inclusive)')
    async def count(self, ctx, start: int, stop: int, *, step: int = 1):
        if ctx.message.author.id == 607583934527569920 or ctx.message.author.id == 509239077212782592:
            global countstop
            countstop = False

            for i in range(start, stop + 1, step):
                if countstop == False:
                    await ctx.send(i)
                else:
                    break

    stopenabled = True

    @commands.command(
        name='stop',
        help=
        'Stops a spamming command given the command name (there might be a few second delay), works for kaczynskifull, kaczynskifulldm, quranfullmsg, count'
    )
    async def stop(self, ctx, command):
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

    @commands.command(
        name='stoptoggle',
        help=
        'Toggles between whether c.stop works or not (Only usable by Cocánb Altort)\n\nThe <stoptoggle> argument can be either \'enable\', \'disable\' or \'query\' and the command resets every time the bot is restarted.'
    )
    async def stoptoggle(self, ctx, stoptoggle):
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


async def setup(bot):
    await bot.add_cog(Messages(bot))