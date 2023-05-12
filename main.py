import keep_alive
import os
import openai
import pyqrcode
from aiogram import Bot, Dispatcher, executor, types
import logging
import random
from stories import *
from config import *

version = 0.1.4

bot = Bot(token=Token)
dp = Dispatcher(bot)
#openai.api_key = "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"

logging.basicConfig(format='%(asctime)s - %(message)s - %(name)s', level=logging.INFO)

@dp.message_handler(commands=['start'])
async def welcome(message : types.Message):
    await message.reply(start_message)

@dp.message_handler(commands=["help"])
async def help(message : types.Message):
  await message.reply("How can i help you? this bot is in development right now!)

@dp.message_handler(commands=['about'])
async def about(message : types.Message):
  await message.reply(f"Hello there! I'm a private bot made for {group_name}")

@dp.message_handler(commands=['join'])
async def join(message : types.Message):
    await message.reply(f"here you can join us : {group_link}")

@dp.message_handler(commands=['status'])
async def status(message : types.Message):
  group=group_status
  if group==True:
    await message.reply("The current status of group is : active\nUse /join to get link of the group multiverse.")
  else :
    await message.reply(f"The current status of group is : Banned")


@dp.message_handler()
async def message(message : types.Message):
  time=datetime.datetime.now()
  if admin==config.admin_id:
    for j in config.listid:
      try :
        await bot.send_message(chat_id=j,text=message.text)
      except Exception as e:
        print(e)
    await bot.send_message(chat_id=message.chat.id, text="Message send")
  if config.key!=" " and config.key!="":      
    if message.text==config.key:
        id=str(message.chat.id)
        if id[0]!="-":
            await bot.send_message(chat_id=message.chat.id,text=config.group_link)
            logging.info(f"{message.from_user.username} requested for {config.group_name}.")
            file = open("chat_log.txt","a")
            file.write(f"{time} - {message.from_user.username} requested for the {config.group_name}")                    
  else :
    logging.info(f"{message.from_user.first_name} ({message.chat.id} {message.from_user.username}): {message.text}")
    file=open("chat_log.txt","a")
    file.write(f"{time} - {message.from_user.first_name} ({message.chat.id} {message.from_user.username}): {message.t
keep_alive.keep_alive()
try :
  if __name__=="__main__": 
    logging.info("Starting bot...")
    logging.info("Bot started")
    executor.start_polling(dp)
    bot.sendMessage
    logging.info("Bot stopped")
except Exception as e:
    print(e)
