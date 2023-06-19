from discord.ext import commands


class Testing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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


async def setup(bot):
    await bot.add_cog(Testing(bot))
