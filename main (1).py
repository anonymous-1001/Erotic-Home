import keep_alive
import os
import openai
import pyqrcode
from aiogram import Bot, Dispatcher, executor, types
import logging
import random
from stories import *
import textwrap
import mysql.connector
import config
import datetime

"""
version = 0.1.4
This bot is only for educations purpose.
"""

#I hide my token! so you can only see the code not my bot token.
bot = Bot(token=os.getenv("Token"))
dp = Dispatcher(bot)

logging.basicConfig(format='%(asctime)s - %(message)s - %(name)s',level=logging.INFO)

#Commands block
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
  await message.reply(
    "Hello, i am bot for the private use of group 'Erotic Home.'\n use /help to know more"
  )


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
  await message.reply("how can i help ?\nCommands list is given below.")

@dp.message_handler(commands=['about'])
async def about(message: types.Message):
  await message.reply("Hello there! I'm a private bot.")


@dp.message_handler(commands=['join'])
async def join(message: types.Message):
  #text = pyqrcode.create(message.text)
  #text.png('myqr.png', scale=5)
  #await bot.send_photo(chat_id=message.chat.id, photo=open('myqr.png', 'rb'))
  await message.reply(f"here you can join us : {config.group_link}")
  logging.info(f"{message.from_user.usernwme} requested for public group link.")

@dp.message_handler(commands=['status'])
async def status(message: types.Message):
  group = config.group_status
  if group == True:
    await message.reply(
      "The current status of group is : active\nUse /join to get link of the group."
    )
  else:
    await message.reply("The current status of group is : ban")

@dp.message_handler(commands=['story'])
async def stories(message: types.Message):
  X = random.choice(story)
  if len(X) <= 4096:
    await message.reply(X)
  else:
    textwrap.wrap(X, width=4000)

@dp.message_handler(commands=['demo'])
async def video(message : types.Message):
  vidlist=["vids/3.mp4","vids/5.mp4","vids/1.mp4","vids/2.mp4","vids/4.mp4"]
  for i in vidlist:
    vid=open(i,"rb")
    await bot.send_video(chat_id=message.chat.id,video=vid)

@dp.message_handler(commands=['id'])
async def id(message : types.Message):
  id=str(message.chat.id)
  if id[0]=="-":
    await bot.send_message(chat_id=id,text=f"group id : {message.chat.id}")
  else:
    await bot.send_message(chat_id=id,text=f"user id : {message.chat.id}")

#custom command
@dp.message_handler()
async def message(message : types.Message):
  admin=False
  time=datetime.datetime.now()
  for i in config.admin_id:
    if message.chat.id==i:
      admin=True
      break
  if admin==True:
    for j in config.listid:
      try :
        await bot.send_message(chat_id=j,text=message.text)
      except Exception as e:
        print(e)
    await bot.send_message(chat_id=message.chat.id, text="Message send")

  if message.text=="Kxy1776.2023@EHAGGJ":
    id=str(message.chat.id)
    if id[0]!="-":
      #await #bot.appr(chat_id=-1001971922628,user_id=message.chat.id)
      await bot.send_message(chat_id=message.chat.id,text="https://t.me/+3-lqW-U-7mM2NTI1")
      logging.info(f"{message.from_user.username} requested for Erotic Home main.")
      file = open("chat_log.txt","a")
      file.write(f"{time} - {message.from_user.username} requested for the Erotic Home Main")
  else :
    logging.info(f"{message.from_user.first_name} ({message.chat.id} {message.from_user.username}): {message.text}")
    file=open("chat_log.logs","a")
    file.write(f"{time} - {message.from_user.first_name} ({message.chat.id} {message.from_user.username}): {message.text}\n")
    
keep_alive.keep_alive()
try:
  if __name__ == "__main__":
    logging.info("Starting bot...")
    logging.info("Bot started")
    executor.start_polling(dp)
    logging.info("Bot stopped")
except Exception as e:
  print(e)
