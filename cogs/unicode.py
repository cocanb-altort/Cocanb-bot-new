import textwrap
import unicodedata

import discord
from discord.ext import commands


class Unicode(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tochar',
                      help='Converts unicode codepoints to characters')
    async def tochar(self, ctx, *, codepoint):
        codepoints = codepoint.split(' ')
        responses = list()
        for i in range(len(codepoints)):
            i_dec = int(codepoints[i], 16)
            response = chr(i_dec)
            ''' for surrogate chars (failed)
      else:
        my_text = docx2txt.process("Resources/surrogate chars.docx")
        surrogate_char_list = my_text.split("\n")
        response = surrogate_char_list[i_dec-55296]
      '''
            responses.append(response)
        responses = ''.join(responses)
        await ctx.send('`' + responses + '`')

        embed = discord.Embed(title="Hold to copy then delete the final ←",
                              description=responses + '←')

        await ctx.send(embed=embed)
        '''
    components = [Button(label="Copy (WIP)", custom_id="button1")])
    while True:
      interaction = await self.bot.wait_for("button_click")
      await interaction.send(content = "Copied to clipboard (WIP)", ephemeral = True)
    '''

    @commands.command(name='tocode',
                      help='Converts character to unicode codepoint')
    async def tocode(self, ctx, *, character):
        characters = list(character)
        responses = list()
        for i in range(len(characters)):
            if len(
                    characters[i]
            ) == 3 and characters[i][0] == '`' and characters[i][2] == '`':
                characters[i] = characters[i][1]
            elif len(character) == 7 and characters[i][
                    0:3] == '```' and characters[i][4:7] == '```':
                characters[i] = characters[i][3]
            else:
                characters[i] = characters[i]
            response = hex(ord(characters[i]))
            response = response[2:]
            if len(response) == 1:
                response = '000' + response
            elif len(response) == 2:
                response = '00' + response
            elif len(response) == 3:
                response = '0' + response
            elif len(response) == 5:
                response = '0' + response
            else:
                pass
            code = response
            response = code.upper()
            responses.append(response)
        responses = ' '.join(responses)
        responses_extra = textwrap.wrap(responses, 1994)
        for i in responses_extra:
            await ctx.send('```' + i + '```')

    @commands.command(name='todesc',
                      help='Converts unicode codepoint to description')
    async def todesc(self, ctx, codepoint):
        char = chr(int(codepoint, 16))
        try:
            await ctx.send(unicodedata.name(char))
        except:
            await ctx.send('<no description>')

    @commands.command(
        name='unicode',
        help=
        'Sends full unicode chart\n\nSupported file formats: .zip, .rar, .tar.gz or .jar file'
    )
    async def unicode(self, ctx, format: str = 'zip'):
        if format == 'zip' or format == '.zip':
            with open("Resources/Full Unicode Charts/Full Unicode Chart.zip",
                      "rb") as file:
                await ctx.send("Full Unicode Chart.zip",
                               file=discord.File(file,
                                                 "Full Unicode Chart.zip"))
        elif format == 'rar' or format == '.rar':
            with open("Resources/Full Unicode Charts/Full Unicode Chart.rar",
                      "rb") as file:
                await ctx.send("Full Unicode Chart.rar",
                               file=discord.File(file,
                                                 "Full Unicode Chart.rar"))
        elif format == '.tar.gz' or format == 'tar.gz' or format == 'targz' or format == 'gz' or format == '.gz':
            with open(
                    "Resources/Full Unicode Charts/Full Unicode Chart.tar.gz",
                    "rb") as file:
                await ctx.send("Full Unicode Chart.tar.gz",
                               file=discord.File(file,
                                                 "Full Unicode Chart.tar.gz"))
        elif format == 'jar' or format == '.jar':
            with open("Resources/Full Unicode Charts/Full Unicode Chart.jar",
                      "rb") as file:
                await ctx.send("Full Unicode Chart.jar",
                               file=discord.File(file,
                                                 "Full Unicode Chart.jar"))
        else:
            await ctx.send("Invalid format")

    @commands.command(
        name='ucsur',
        help=
        'Converts toki pona words into UCSUR codepoints.\n\nWords supported: all nimi ku suli + pake, apeja, majuna, powe\n\nTo use this command, separate everything with spaces, including punctuation and control characters\n\nTo use a cartouche, put "[" and "]" before and after the whole name, and "=" after every word, for example:\n  [ nimi = nimi = nimi = ]\n\nTo use long pi, replace the "pi" with "|", then put _ after every word, for example:\n  nimi | nimi _ nimi _\n\nPunctuation supported: "." and ":"\n\nControl characters supported (for usage refer to UCSUR standard):\n  "stack": stacking joiner\n  "scale": scaling joiner\n  "slg"/"elg": start/end of long glyph\n  "lge": combining long glyph extension\n  "srlg"/"erlg": start/end of reverse long glyph'
    )
    async def ucsur(self, ctx, *, tokipona):
        allkuwords = "a akesi ala alasa ale anpa ante anu awen e en esun ijo ike ilo insa jaki jan jelo jo kala kalama kama kasi ken kepeken kili kiwen ko kon kule kulupu kute la lape laso lawa len lete li lili linja lipu loje lon luka lukin lupa ma mama mani meli mi mije moku moli monsi mu mun musi mute nanpa nasa nasin nena ni nimi noka o olin ona open pakala pali palisa pan pana pi pilin pimeja pini pipi poka poki pona pu sama seli selo seme sewi sijelo sike sin sina sinpin sitelen sona soweli suli suno supa suwi tan taso tawa telo tenpo toki tomo tu unpa uta utala walo wan waso wawa weka wile namako kin oko kipisi leko monsuta tonsi jasima kijetesantakalu soko meso epiku kokosila lanpan n misikeke ku"
        kulist = allkuwords.split(" ")

        kudict = {}
        for i in range(len(kulist)):
            kudict[kulist[i]] = chr(int("F1900", 16) + i)
        kudict.update({
            'ali': '\U000f1904',
            '[': '\U000f1990',
            ']': '\U000f1991',
            '=': '\U000f1992',
            '|': '\U000f1993',
            '_': '\U000f1994',
            'stack': '\U000f1995',
            'scale': '\U000f1996',
            'slg': '\U000f1997',
            'elg': '\U000f1998',
            'lge': '\U000f1999',
            'srlg': '\U000f199a',
            'erlg': '\U000f199b',
            '.': '\U000f199c',
            ':': '\U000f199d',
            'pake': '\U000f19a0',
            'apeja': '\U000f19a1',
            'majuna': '\U000f19a2',
            'powe': '\U000f19a3'
        })

        tokiponawords = tokipona.split(' ')
        ucsur = ''
        for i in range(len(tokiponawords)):
            if tokiponawords[i] in kudict:
                ucsur += kudict[tokiponawords[i]]
            else:
                ucsur += '*'
        await ctx.send(ucsur)

    @commands.command(
        name='mapids',
        help=
        'Converts toki pona words into minecraft map ids on the Cocánb Minecraft server.\n\nWords supported: all nimi ku suli + pake, apeja, majuna, powe\n\nTo use this command, separate everything with spaces, including punctuation below.\n\nPunctuation supported:\nOpening cartouche: type [\nClosing cartouche: type ]\nCartouche bracket: type = (Use not recommended)\nStart of long pi: type | (Use not recommended)\nLong pi bracket: type _ (Use not recommended)\nPeriod/Full stop: type .\nColon: type :\nSpace: type space\nCocánb symbol: type cocanb\n\nTo get map item, take each number and put them into the command "/give @s filled_map{map:[map_id]}" one at a time, replacing "[map_id]" with the numbers.'
    )
    async def mapids(self, ctx, *, tokipona):
        allkuwords = "a akesi ala alasa ale anpa ante anu awen e en esun ijo ike ilo insa jaki jan jelo jo kala kalama kama kasi ken kepeken kili kiwen ko kon kule kulupu kute la lape laso lawa len lete li lili linja lipu loje lon luka lukin lupa ma mama mani meli mi mije moku moli monsi mu mun musi mute nanpa nasa nasin nena ni nimi noka o olin ona open pakala pali palisa pan pana pi pilin pimeja pini pipi poka poki pona pu sama seli selo seme sewi sijelo sike sin sina sinpin sitelen sona soweli suli suno supa suwi tan taso tawa telo tenpo toki tomo tu unpa uta utala walo wan waso wawa weka wile namako kin oko kipisi leko monsuta tonsi jasima kijetesantakalu soko meso epiku kokosila lanpan n misikeke ku"
        kulist = allkuwords.split(" ")

        kudict = {}
        for i in range(len(kulist)):
            kudict[kulist[i]] = str(500 + i)

        kudict.update({
            'ali': '504',
            '[': '644',
            ']': '645',
            '=': '646',
            '|': '647',
            '_': '648',
            '.': '656',
            ':': '657',
            'pake': '660',
            'apeja': '661',
            'majuna': '662',
            'powe': '663',
            'space': '658',
            'cocanb': '81'
        })

        tokiponawords = tokipona.split(' ')
        ucsur = ''
        for i in range(len(tokiponawords)):
            if tokiponawords[i] in kudict:
                ucsur += kudict[tokiponawords[i]] + ' '
            else:
                ucsur += '* '
        await ctx.send(ucsur)


async def setup(bot):
    await bot.add_cog(Unicode(bot))
