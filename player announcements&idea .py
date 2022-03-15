import disnake
from disnake.ext import commands

token = ''
bot = commands.Bot(command_prefix='*')

''' 
Этот бот нужен для отправки объявлений от игроков в определенный канал.

Изменить строки
16 гильдия в которой будет проверяться роль, изменить id
20 id роли на которую будет проверка, изменить id | да убогое решение, но по мне это быстрее, чем правильная проверка
22 канал куда будут отправляться объявления игроков, изменить id
4 токен, но это банальность 
'''

# не обращайте внимание на мой русский, текст вы всегда можете изменить сами. https://imgur.com/sxyQ2Uy
@commands.dm_only()
@bot.command(aliases=['объявления', 'Объявления', 'творка', 'Творка'])
async def tvorka(ctx, *, texttv):
    global message
    guild = bot.get_guild(id)
    embed = disnake.Embed(title='Творка', description=texttv)
    try:
        member = await guild.fetch_member(ctx.author.id)
        if 'id' in str(member.roles):
            channel = bot.get_channel(id)
            if ctx.message.attachments:
                embed.set_image(url=ctx.message.attachments[0].url)
                message = await channel.send(embed=embed)
            else:
                message = await channel.send(embed=embed)
            embed2 = disnake.Embed(title="Спасибо", description="Ура, ваше сообщение опубликованно!\n"
                                                                f"Вот ссылка на него - [тык]({message.jump_url})")
            await ctx.reply(embed=embed2)
        else:
            await ctx.send("Похоже, у вас нет проходки.")
    except:
        await ctx.send("Похоже, у вас нету в нашей гильдии.")
        
# не вижу смысла делать в разных файлах, ведь 1 и тоже.     
@bot.command(aliases=['идея', 'Идея'])
async def idea(ctx, *, idea):
    global message
    guild = bot.get_guild(948660312280817764)
    embed = disnake.Embed(title='Идея', description=idea)
    try:
        member = await guild.fetch_member(ctx.author.id)
        if '952365239712747581' in str(member.roles):
            channel = bot.get_channel(949268141836496957)
            if ctx.message.attachments:
                embed.set_image(url=ctx.message.attachments[0].url)
                message = await channel.send(embed=embed)
            else:
                message = await channel.send(embed=embed)
            embed2 = disnake.Embed(title="Спасибо", description="Ура, ваша идея опубликованно!\n"
                                                                f"Вот ссылка на него - [тык]({message.jump_url})")
            await ctx.reply(embed=embed2)
            await message.create_thread(name=f'Идея {ctx.author.name}', auto_archive_duration=None)
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        else:
            await ctx.send("Похоже, у вас нет проходки.")
    except:
        await ctx.send("Похоже, у вас нету в нашей гильдии.")


bot.run(token)
