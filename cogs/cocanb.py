import discord
from discord.ext import commands

from Translate import toc as t
from Translate import translator

# NOTE: non-existent module
import cocanb


class Cocánb(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cocanb',
                      help='Sends thPoéo thCocán Altorn Onécmdf Bec Bftf')
    async def cocanb(self, ctx, format: str = None):
        if format is None:
            await ctx.send(
                'thPoéo thCocán Altorn Onécmdf Bec Bftf\n\nCocánb altort, ürpenîtort ürodictort ürişêxu áaç tivitin volvinãp plicat īóopaioc onşt rictiot thpení otês ticlen onkdd cłdeğse egřbk degsbáal fýhginkf bňdřbň lobec seřbsi. Thîmain vòlvdir ectlpá infuác tiviti, esücağ énitap iercinŵap, lagenít, aspan, kiñşqué ezinb, albüs tingen, itafløg, ginürethrap, latickłt ortú, rerotielec trøstim ulatiok, néeinok ickinnons dýce gýhlgşjħd sbłggħx cýdłggh gildggłg ghlhýd efegč fňřg gřbgg. Thrécipie nosûcác tiviti émareç eivdir ecphýş icaple asurvim asochísœ, motionâp leasürt hrouğe rôti chumili, atióok noŵledgt hath plaipléa sint sadis tidomin antnon ectifbh dşjýčeğtflħe hačmir bliehhğclčfň křbeit decýds bgho báachth. Manóth éspraç tičecarrsiğ nifîca nħéal trisk nonýdf béesi yetkħfse.'
            )
        elif format == 'ipa':
            await ctx.send(
                '[θ‿poˈe̯.o̞̯ θ‿koˈkɐn älˈtorn‿ɔnɛkm̩df bek.ˈbf̩tf̩]\n\n[ko̞ˈkɐnb ʔälˈtort | ˈʔyrpeni̞ˌtort‿yrodi̞k̚ˈtort‿yrɪʃe̞ksu ʔʌsˑ ˌtɪvɪˈtʲɪn vɤɫviˈnʌ̃ᵐp pliˈkɐt joːpɐˈjok‿on̠ʃt ri̞kˈtʲjot θ‿ˈpe̞ni o̞ˈte̙ʃ ‖ ti̞klen ʔo̞ŋkt | kl̩ˈdeɪ̯s̬ə‿eˈɡr̩b̥k deg̊sˈbaˑɫ fy̞̆ˈgi̞nk͡f | ˈbn̩dr̩ˌbn̩ lɔ̞ˈbe̞k̚ ˈse̞.r̩b.siˑ ‖ tʰɪˈmɐɪ̯n vo̞ɫvˈdiːr ekt͡ɬˈpä ɪnˈfʷɐk̚ tiviˈtʲiː | e̞sʉˈkäɪ̯ e̞nɪ̆ˈtäp̚ jɤrt͡ʃinˈwɐp̚ | läʒe̽ni̞t | ɐsˈpɐn | ˈki̞n̠ʃke‿eˌz̥inb | älˈbys tiˈŋe̽n | i̞täfløɡ̟ | gi̞nʲʏ̙rəˈθr̥ɐp̚ | lɐˈti̞kl̩t‿ɔrˌtu | re̞roˈtʲjelɪk t̪ʰr̥østim uläˈtʲjɔk̚ ‖ neɪ̯no̞k ɪkĭ̞ˈnˑɔns dʲyke ˈgɪɫgʃ̟ɯ̽̆d ˈsb̥ɫ̩gɯ̽̆ks ˈkʰɪdɫ̩g ˈgɪɫdgɫ̩g ˈglɪd | e̞fe̞t͡ʃʰ fn̩ˈr̩g gr̩b̥g̊ ‖ θr̥esiˈpiː nosuˈkɐk̚ tivitʲiˑ‿e̞mäˈresˑ‿eɪ̯vˈdir‿ekˈfi̞s‿iˈkapl‿ɐsʊrˈvɪm‿ɐso̞t͡ʃɪ̆sœː | motʲjoˈnɐp̚ le.ɐˈsɯ̽rt r̥uːd͡ʒ roˈtʲi t͡ʃʊmɪliː ‖ ɐtʲjʊ̆k̚ noˑˈle̞d̥ktʰ hɐθ plɐɪ̯ˈpleːɐ̯ sɪnt ˈsädɪs ti̞do̞ˈmɪn ɐntʰˈnɔn ɛkˈti̞v d͡ʒɨˈt͡ʃetfle hɐt͡ʃˈmiːr bleɪ̯t͡ʃʒ̩̊̆t͡ʃfn̩ kr̩ˈbɐɪ̯t̚ deˈki̞d̥s bˠo bɐt͡ʃθ ‖ mäˈnɔθ‿esˌprɑːk̚ tɪt͡ʃə̆ˈkɐrse̽ɪ ˈnɪfɪkä n̥eːɐ̯ɫ t̪ʰr̥ɪskʰ | nɔˈnɪd͡f beːs̬i ˈjetkfsɛː]'
            )
        elif format == 'braille':
            await ctx.send(
                '⠞⠓⠠⠏⠕⠑⠕⠀⠞⠓⠠⠉⠕⠉⠁⠝⠀⠠⠁⠇⠞⠕⠗⠝⠀⠠⠕⠝⠑⠉⠍⠙⠋⠀⠠⠃⠑⠉⠀⠠⠃⠋⠞⠋\n\n⠠⠉⠕⠉⠁⠝⠃⠀⠁⠇⠞⠕⠗⠞⠂⠀⠥⠗⠏⠑⠝⠊⠞⠕⠗⠞⠀⠥⠗⠕⠙⠊⠉⠞⠕⠗⠞⠀⠥⠗⠊⠎⠑⠭⠥⠀⠁⠁⠉⠀⠞⠊⠧⠊⠞⠊⠝⠀⠧⠕⠇⠧⠊⠝⠁⠏⠀⠏⠇⠊⠉⠁⠞⠀⠊⠕⠕⠏⠁⠊⠕⠉⠀⠕⠝⠎⠞⠀⠗⠊⠉⠞⠊⠕⠞⠀⠞⠓⠏⠑⠝⠊⠀⠕⠞⠑⠎⠀⠞⠊⠉⠇⠑⠝⠀⠕⠝⠅⠙⠙⠀⠉⠇⠙⠑⠛⠎⠑⠀⠑⠛⠗⠃⠅⠀⠙⠑⠛⠎⠃⠁⠁⠇⠀⠋⠽⠓⠛⠊⠝⠅⠋⠀⠃⠝⠙⠗⠃⠝⠀⠇⠕⠃⠑⠉⠀⠎⠑⠗⠃⠎⠊⠲⠀⠠⠞⠓⠊⠍⠁⠊⠝⠀⠧⠕⠇⠧⠙⠊⠗⠀⠑⠉⠞⠇⠏⠁⠀⠊⠝⠋⠥⠁⠉⠀⠞⠊⠧⠊⠞⠊⠂⠀⠑⠎⠥⠉⠁⠛⠀⠑⠝⠊⠞⠁⠏⠀⠊⠑⠗⠉⠊⠝⠺⠁⠏⠂⠀⠇⠁⠛⠑⠝⠊⠞⠂⠀⠁⠎⠏⠁⠝⠂⠀⠅⠊⠝⠎⠟⠥⠑⠀⠑⠵⠊⠝⠃⠂⠀⠁⠇⠃⠥⠎⠀⠞⠊⠝⠛⠑⠝⠂⠀⠊⠞⠁⠋⠇⠕⠛⠂⠀⠛⠊⠝⠥⠗⠑⠞⠓⠗⠁⠏⠂⠀⠇⠁⠞⠊⠉⠅⠇⠞⠀⠕⠗⠞⠥⠂⠀⠗⠑⠗⠕⠞⠊⠑⠇⠑⠉⠀⠞⠗⠕⠎⠞⠊⠍⠀⠥⠇⠁⠞⠊⠕⠅⠂⠀⠝⠑⠑⠊⠝⠕⠅⠀⠊⠉⠅⠊⠝⠝⠕⠝⠎⠀⠙⠽⠉⠑⠀⠛⠽⠓⠇⠛⠎⠚⠓⠙⠀⠎⠃⠇⠛⠛⠓⠭⠀⠉⠽⠙⠇⠛⠛⠓⠀⠛⠊⠇⠙⠛⠛⠇⠛⠀⠛⠓⠇⠓⠽⠙⠀⠑⠋⠑⠛⠉⠀⠋⠝⠗⠛⠀⠛⠗⠃⠛⠛⠲⠀⠠⠞⠓⠗⠑⠉⠊⠏⠊⠑⠀⠝⠕⠎⠥⠉⠁⠉⠀⠞⠊⠧⠊⠞⠊⠀⠑⠍⠁⠗⠑⠉⠀⠑⠊⠧⠙⠊⠗⠀⠑⠉⠏⠓⠽⠎⠀⠊⠉⠁⠏⠇⠑⠀⠁⠎⠥⠗⠧⠊⠍⠀⠁⠎⠕⠉⠓⠊⠎⠕⠑⠂⠀⠍⠕⠞⠊⠕⠝⠁⠏⠀⠇⠑⠁⠎⠥⠗⠞⠀⠓⠗⠕⠥⠛⠑⠀⠗⠕⠞⠊⠀⠉⠓⠥⠍⠊⠇⠊⠂⠀⠁⠞⠊⠕⠕⠅⠀⠝⠕⠺⠇⠑⠙⠛⠞⠀⠓⠁⠞⠓⠀⠏⠇⠁⠊⠏⠇⠑⠁⠀⠎⠊⠝⠞⠀⠎⠁⠙⠊⠎⠀⠞⠊⠙⠕⠍⠊⠝⠀⠁⠝⠞⠝⠕⠝⠀⠑⠉⠞⠊⠋⠃⠓⠀⠙⠎⠚⠽⠉⠑⠛⠞⠋⠇⠓⠑⠀⠓⠁⠉⠍⠊⠗⠀⠃⠇⠊⠑⠓⠓⠛⠉⠇⠉⠋⠝⠀⠅⠗⠃⠑⠊⠞⠀⠙⠑⠉⠽⠙⠎⠀⠃⠛⠓⠕⠀⠃⠁⠁⠉⠓⠞⠓⠲⠀⠠⠍⠁⠝⠕⠞⠓⠀⠑⠎⠏⠗⠁⠉⠀⠞⠊⠉⠑⠉⠁⠗⠗⠎⠊⠛⠀⠝⠊⠋⠊⠉⠁⠀⠝⠓⠑⠁⠇⠀⠞⠗⠊⠎⠅⠀⠝⠕⠝⠽⠙⠋⠀⠃⠑⠑⠎⠊⠀⠽⠑⠞⠅⠓⠋⠎⠑⠲'
            )
        elif format == "french" or format == "français":
            await ctx.send(
                'sPeaux-é-eaux sCocâne Altorne Eaux-néceumdfe Bèque Beufteuf\n\nCocânbe altorte, urpénitorte ureaudictorte urichècsous asse tivitine vaulvinampe plicâte yeaupaïeauc onchte rictiaute spénie hautèche ticlènne ôncde, ceuldaiseux egueurbque dègsse-bâle fuguinncf beundeurbeun laubèque séreubssie. Timaïn vaulvdire écteulpa îne-fouaque tivitie, éssucaïe enitâpe yeur-tchinne-ouâpe, la-jénitte assepâne, quinnche-qué ésinbe, albusse tingènne, itafleugue, guinurésrâppe, laticeult aurtout, réraux-tiéleque treusse-tîme oulatieauque, néneauque iquinnonnsse dûqué guilgue-cheude sbeul-geucsse quideulge guilde-geulgue glide efètche feuneurgue geurbgue. Sréssipie neaussoucaque tivitie émaresse aivdire écfisse icaple asourvime asseautchissœux, mautieaunâppe léasurte chrouge rôtie tchoumilie, atieauque naulèdgte hâsse plaïe-pléa sinnte sadisse tidaumine annte-nonne éctive djeu-tchètte-flais hâtchmire blaitcheutchfeunne cœurbaïte déquidsse breaux bâtchsse. Mâneausse ésse-prâque titchais-carre-sais nificât néale trisque neaunidfe béesie yètqueufsais.'
            )
        elif format == "backwards":
            await ctx.send(
                '.esfħktey iseéb fdýnon ksirt laéħn acîfin ğisrracečit çarpsé htónaM .hthcaáb ohgb sdýced tiebřk ňfčlcğhheilb rimčah eħlftğečýjşd hbfitce nontna nimodit sidas tnis aélpialp htah tgdelŵon koóita ,ilimuhc itôr eğuorh trüsael pânoitom ,œsíhcosa mivrusa elpaci şýhpce ridvie çeramé itivit cácûson eipicérhT .ggbřg gřňf čgefe dýhlhg głggdlig hggłdýc xħggłbs dħjşglhýg ecýd snonnikci konieén ,koitalu mitsørt celeitorer ,útro tłkcital ,parhterünig ,gølfati ,negnit sübla ,bnize éuqşñik ,napsa ,tínegal ,paŵnicrei patiné ğacüse ,itivit cáufni ápltce ridvlòv niamîhT .isbřes cebol ňbřdňb fknighýf laábsged kbřge esğedłc ddkno nelcit sêto ínepht toitcir tşno coiapoóī tacilp pãnivlov nitivit çaá uxêşirü trotcidorü trotîneprü ,trotla bnácoC\n\nftfB ceB fdmcénO nrotlA nácoCht oéoPht'
            )
        elif format == "audio":
            with open("Resources/thPoéo pronunciation audio.mp3",
                      "rb") as file:
                await ctx.send(
                    "thPoéo thCocán Altorn Onécmdf Bec Bftf pronunciation guide",
                    file=discord.File(
                        file,
                        "thPoéo thCocán Altorn Onécmdf Bec Bftf pronunciation guide"
                    ))
        else:
            await ctx.send('Invalid format')

    @commands.command(
        name="deltoc",
        help="In beta: Translate message into Cocánb (deletes original message)"
    )
    async def deltoc(self, ctx, *args):
        try:
            arg = ' '.join(args)

            arg = arg.replace(".", " . ")
            arg = arg.replace(",", "")
            arg = arg.replace("!", " ! ")
            arg = arg.replace("?", " ? ")

            templ = list(arg)
            for x in range(len(templ)):
                templ[x] = templ[x].lower()

            final = t.handleSentences(''.join(templ))
            await ctx.message.delete()
            await ctx.send('[{.author.mention}]: '.format(ctx) + final)
        except:
            await ctx.send("Insufficient permissions.")

    @commands.command(
        name="toc",
        help="Defunct: Translates message into Cocánb (keeps original message)"
    )
    async def toc(self, ctx, *args):
        arg = ' '.join(args)

        arg = arg.replace(".", " . ")
        arg = arg.replace(",", "")
        arg = arg.replace("!", " ! ")
        arg = arg.replace("?", " ? ")

        templ = list(arg)
        for x in range(len(templ)):
            templ[x] = templ[x].lower()

        final = t.handleSentences(''.join(templ))
        await ctx.send(final)

    @commands.command(
        name='toctest',
        help=
        'Translates message into Cocánb (keeps original message) (Please use this command instead of c.toctest)'
    )
    async def toctest(self, ctx, *, sentence):
        await ctx.send(translator.ctranslate(sentence))

    @commands.command(name='bettertoc',
                      help='English to Cocánb by someone who can actually code'
                      )
    async def bettertoc(self, ctx, *, sentence):
        await ctx.send(cocanb.english_to_cocanb(sentence))

    @commands.command(name='bettertoe',
                      help='Cocánb to English by someone who can actually code'
                      )
    async def bettertoe(self, ctx, *, sentence):
        await ctx.send(cocanb.cocanb_to_english(sentence))

    @commands.command(
        name="script",
        help=
        "Sends the Cocánb symbols\nSupported: cocanb/cocánb, cock, and, ball, torture, shit, cringe, constriction, onomatopoeia/onomatopœia, altort, why cello there, roux for eternity, monkey/monke, tatrapomar, amogus, mute, kick, ban\n(Words separated with / output the same thing)"
    )
    async def script(self, ctx, *, word):
        word = word.lower()
        if word == "cocanb" or word == "cocánb":
            await ctx.send("<:cocanb:812322440351842365>")
        elif word == "cock":
            await ctx.send("<:cock:794451604278870026>")
        elif word == "and":
            await ctx.send("<:and:794451630194950174>")
        elif word == "ball":
            await ctx.send("<:ball:794451654098419712>")
        elif word == "torture":
            await ctx.send("<:torture:794451672641961985>")
        elif word == "shit":
            await ctx.send("<:shit:806451654362136606>")
        elif word == "cringe":
            await ctx.send("<:cringe:801335612699181056>")
        elif word == "constriction":
            await ctx.send("<:constriction:794505293333266432>")
        elif word == "onomatopoeia" or word == "onomatopœia":
            await ctx.send("<:onomatopoeia:810395187372752946>")
        elif word == "altort":
            await ctx.send("<:altort:806454273935933460>")
        elif word == "why cello there":
            await ctx.send("<:why_cello_there:817021579878858802>")
        elif word == "roux for eternity":
            await ctx.send("<:roux_for_eternity:817181369137627186>")
        elif word == "monkey" or word == "monke":
            await ctx.send("<:monkey:817404046762704946>")
        elif word == "tatrapomar":
            await ctx.send("<:tatrapomar:817413408370065468>")
        elif word == "amogus":
            await ctx.send("<:amogus:813328288332251137>")
        elif word == "mute":
            await ctx.send("<:mute:819548998297583617>")
        elif word == "kick":
            await ctx.send("<:kick:819548910883569685>")
        elif word == "ban":
            await ctx.send("<:ban:819548958707023892>")
        else:
            await ctx.send("This word has not been created yet.")

    @commands.command(
        name='guide',
        help='Sends a guide on how to speak Cocánb (doc guide or video guide)')
    async def guide(self, ctx, format='doc'):
        if format == 'doc' or format == 'document':
            await ctx.send(
                'https://docs.google.com/document/d/1AwVWizqoL6YsQME7EQLwZO9AB8YLdsNQ0zDVY1bDaeQ/edit?usp=drivesdk'
            )
        elif format == 'video':
            await ctx.send('https://youtu.be/GSCpGW5EiKo')
        else:
            await ctx.send('Invalid format')

    @commands.command(
        name='language',
        help=
        'Sends the name for "Cocánb" in different languages\n\nSupported languages: English, French, Spanish, Portugese, German, Swedish, Finnish, Czech, Polish, Traditional Chinese, Simplified Chinese, Japanese, Korean, Russian, Greek, Arabic, Sanskrit/Hindi Devenagari, Malayalam, Cocánb'
    )
    async def language(self, ctx, lang):
        lang = lang.lower()
        if lang == "english":
            await ctx.send("Cocánb")
        elif lang == "french":
            await ctx.send("Cocânbe")
        elif lang == "spanish":
            await ctx.send("Cocánb")
        elif lang == "portugese":
            await ctx.send("Concanês")
        elif lang == "german":
            await ctx.send("Bischochaisch")
        elif lang == "swedish":
            await ctx.send("Kåkanb")
        elif lang == "finnish":
            await ctx.send("Kokaanbi")
        elif lang == "czech":
            await ctx.send("Kokánb")
        elif lang == "polish":
            await ctx.send("Kokąb")
        elif lang == "chinese" or lang == "traditional chinese" or lang == "trad chinese" or lang == "chinese traditional" or lang == "chinese trad":
            await ctx.send("哥加尼巴")
        elif lang == "simplified chinese" or lang == "chinese simplified" or lang == "sim chinese" or lang == "simp chinese" or lang == "chinese sim" or lang == "chinese sim":
            await ctx.send("哥加尼巴")
        elif lang == "japanese":
            await ctx.send("コカンブ")
        elif lang == "korean" or lang == "corean":
            await ctx.send("코칸브어")
        elif lang == "russian":
            await ctx.send("Коканбский")
        elif lang == "greek":
            await ctx.send("Κοκάνβ")
        elif lang == "arabic":
            await ctx.send("كُكَنب")
        elif lang == "sanskrit" or lang == "sanskrit devenagari":
            await ctx.send("कॉकॅन्ब्")
        elif lang == "hindi" or lang == "hindi devenagari":
            await ctx.send("कौकैन्ब")
        elif lang == "malayalam":
            await ctx.send("കോകാൻബ്")
        elif lang == "tamil":
            await ctx.send("கோகான்பு")
        elif lang == "cocanb" or lang == "cocánb":
            await ctx.send("Cocánn onbf")
        else:
            await ctx.send(
                "Speakers of this language have not yet encountered Cocánb.")

    @commands.command(
        name='keyboard',
        help=
        'Sends a file to download the Cocánb keyboard (Windows)\n\nHow to download keyboard (Windows 10):\nStep 1. Download the file below\nStep 2. Unzip the file\nStep 3. Run \"setup.exe\" and follow required steps\nStep 4. Go to Settings > Time & Language > Language > Add preferred language\nStep 5. Download English (Canada) keyboard\nStep 6. After the download has finished, click on English (Canada) in the preferred languages list and select \"Options\"\nStep 7. Click \"Add a keyboard\" and choose \"Cocánb Keyboard\"\n\nNote: if you downloaded the older version of the keyboard, you have to go to Settings > Add or remove programs and search \"Cocánb\" and delete the old keyboard.\nIf this still doesn\'t work, try again but this time go to File Explorer and delete the source file for the keyboard.'
    )
    async def keyboard(self, ctx):
        with open("Resources/cocaanb.rar", "rb") as file:
            await ctx.send(
                "How to download keyboard (Windows 10):\nStep 1. Download the file below\nStep 2. Unzip the file\nStep 3. Run \"setup.exe\" and follow required steps\nStep 4. Go to Settings > Time & Language > Language > Add preferred language\nStep 5. Download English (Canada) keyboard\nStep 6. After the download has finished, click on English (Canada) in the preferred languages list and select \"Options\"\nStep 7. Click \"Add a keyboard\" and choose \"Cocánb Keyboard\"\n\nNote: if you downloaded the older version of the keyboard, you have to go to Settings > Add or remove programs and search \"Cocánb\" and delete the old keyboard.\nIf this still doesn\'t work, try again but this time go to File Explorer and delete the source file for the keyboard.",
                file=discord.File(file, "Cocánb Keyboard"))

    @commands.command(name='reddit', help='Sends a link to the Cocánb reddit')
    async def reddit(self, ctx):
        await ctx.send(
            'https://www.reddit.com/r/cocanb?utm_medium=android_app&utm_source=share'
        )

    @commands.command(name='wiki', help='Sends a link to the Cocánb Wiki')
    async def wiki(self, ctx):
        await ctx.send(
            'https://cocanb.fandom.com/wiki/ThCoc%C3%A1nwi_knone%C4%87_bf%C3%AEd'
        )


async def setup(bot):
    await bot.add_cog(Cocánb(bot))
