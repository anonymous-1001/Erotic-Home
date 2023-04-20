import keep_alive
import os
import openai
import pyqrcode
from aiogram import Bot, Dispatcher, executor, types
import logging
import random
from stories import *
from config import *

version = 0.1.3

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

@dp.message_handler(commands=['story'])
async def stories(message : types.Message):
  await message.reply(random.choice(story))
@dp.message_handler()
async def message(message : types.Message):
  logging.info(f"{message.from_user.first_name} ({message.chat.id}, {message.from_user.username}):{message.text}")
  
@dp.message_handler()
async def admin(message: types.Message):
  global adminid
  adminid = message.chat.id
  if adminid == admin_id:
    await bot.send_message(chat_id=group_id,text=message.text'
    await message.reply("message is send")

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
