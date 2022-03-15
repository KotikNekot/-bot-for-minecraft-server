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


bot.run(token)
