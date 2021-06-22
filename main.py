from new_counter import NewCounter
from os import name
from counter import Counter
from client_user import Client
from bank import Bank
from discord.ext import commands
import discord
from env import TOKEN
from words import JAMIE_NAMES

bank = Bank('./grock_bank.json')
counter = Counter('./counters.json')
newCounter = NewCounter('./new_counters.json')
bot = commands.Bot(command_prefix='£')

@bot.event
async def on_ready():
    print('Started')

@bot.event
async def on_message(message: discord.Message):
    guild: discord.Guild = message.guild
    if message.author.id == 474605229178880012:
        await message.add_reaction(await guild.fetch_emoji(856632468962934785))

    if message.content[0] == '£':
        await bot.process_commands(message)
        return

    if message.author.bot:
        return

    counters = newCounter.counters
    for i in counters:
        count = message.content.count(i)
        if count != 0:
            newCounter.add(i, count)

    if message.content.lower() in JAMIE_NAMES:
        await message.delete()
    
        channel: discord.TextChannel = message.channel
        await channel.send(f'> (Corrected <@{message.author.id}>): Hail D.a.n')
        await message.author.send('HAILING JAMIE IS NOT PERMITTED')

    elif 'dan' in message.content.lower() :
        channel: discord.TextChannel = message.channel
        await channel.send(f'> HAIL THE SEXY MAN')
        bank.add(Client({'id': message.author.id, 'nick': message.author.nick}), 10)

    # elif 'kenny' in message.content.lower():
    #     kenny_count = message.content.count('kenny')
    #     count = counter.add('kenny', kenny_count)
        # await message.reply(f'> AMONGST OURSELVES FOR TH\' XBOX 360 <@474605229178880012> > kenny has been said {count} times')

    elif '69' in message.content or '420' in message.content:
        await message.reply('nice')

    

@bot.command(name = 'ping')
async def on_ping(ctx: commands.Context):
    message: discord.Message = ctx.message
    await ctx.send(message.author.id)

# @bot.command(name='add')
# async def on_add(ctx: commands.Context, amount: int):
#     message: discord.Message = ctx.message
#     userClient = Client({
#         'id': message.author.id,
#         'nickname': message.author.nick,
#     })

#     bank.add(userClient, amount)

@bot.command(name='bal')
async def on_balance(ctx: commands.Context, member: discord.Member=None):
    if member == None:
        member = ctx.message.author

    user = Client({
        'id': member.id,
        'nickname': member.nick,
    })

    balance = bank.getMoney(user)
    await ctx.send(f'> <@{member.id}> You have {balance} groch')

@bot.command(name='give')
async def give(ctx: commands.Context, amount: int, to: discord.Member):
    if amount <= 0 and not to.id == 474605229178880012:
        await ctx.reply('Fuck you')
        return

    message: discord.Message = ctx.message
    fromClient = Client({
        'id': message.author.id,
        'nickname': message.author.nick,
    })
    toClient = Client({
        'id': to.id,
        'nickname': to.nick
    })

    bank.give(fromClient, toClient, amount)


@bot.command(name='track')
@commands.has_guild_permissions(manage_guild=True)
async def track(ctx: commands.Context, word: str):
    if word not in newCounter.counters:
        newCounter.add_counter(word)
        await ctx.reply(f'> {word} is now being counted.')
    else:
        await ctx.reply(f'> {word} is already being counted')

@bot.command(name='count')
async def count_word(ctx: commands.Context, word: str):
    times = newCounter.get(word)

    await ctx.reply(f'{word} has been said {times} time(s)')
    

bot.run(TOKEN)