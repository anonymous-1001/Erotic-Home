import keep_alive
import os
import openai
import pyqrcode
from aiogram import Bot, Dispatcher, executor, types
import logging
import random
from stories import *

bot = Bot(token='6063405456:AAHlq05bTXsthaDlvr88_YmZB784ihlMbCM')
dp = Dispatcher(bot)
#openai.api_key = "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"

logging.basicConfig(format='%(asctime)s - %(message)s - %(name)s', level=logging.INFO)

'''@dp.message_handler(commands=['send_media'])
async def send_media(message: types.Message):
    # Get the chat ID of the group where the command was sent from
    chat_id = message.chat.id
    
    # Get all media in the group
    media = []
    async for msg in bot.iter_history(chat_id):
      if msg.media:
            media.append(msg.media)
    
    # Get the chat ID of the group to send the media to
      target_chat_id = -1001921874860
    
    # Send the media to the target group
      for m in media:
        await bot.send_media_group(target_chat_id, [m])
    
    # Send a message to confirm the media has been sent
      await message.reply('All media files have been sent to the target group!')
      logging.info("working")
  
'''

@dp.message_handler(commands=['start'])
async def welcome(message : types.Message):
    await message.reply("Hello, i am bot for the private use of group 'Erotic Home.'\n use /help to know more")

@dp.message_handler(commands=["help"])
async def help(message : types.Message):
  await message.reply("how can i help ?\nCommands list is given below.")

@dp.message_handler(commands=['about'])
async def about(message : types.Message):
  await message.reply("Hello there! I'm a private bot.")

@dp.message_handler(commands=['join'])
async def join(message : types.Message):
    #text = pyqrcode.create(message.text)
    #text.png('myqr.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('myqr.png', 'rb'))
    await message.reply("here you can join us : https://t.me/+ggfWVdQ17D43ZmNl")

@dp.message_handler(commands=['status'])
async def status(message : types.Message):
  group=True
  if group==True:
    await message.reply("The current status of group is : active\nUse /join to get link of the group.")
  else :
    await message.reply("The current status of group is : banned")

@dp.message_handler(commands=['story'])
async def stories(message : types.Message):
  await message.reply(random.choice(story))
@dp.message_handler()
async def message(message : types.Message):
  logging.info(f"{message.from_user.first_name} ({message.chat.id}, {message.from_user.username}):{message.text}")
  file = open("chat_logs.txt","a")
  file.write(f"{message.from_user.first_name} ({message.chat.id}, {message.from_user.username}):{message.text}\n")
  
'''async def gpt(message : types.Message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
  )
  await message.reply(response.choice[0].text)
'''

#special command
"""@dp.message_handler()
async def send(message : types.Message):
  if message.text=="send":
    await bot.stend_video(chat_id=message.chat_id, video=open("Incestraja03_1387738582807310340(270P).mp4", "rb"), supports_streaming=True)
    await bot.stend_video(chat_id=message.chat_id, video=open("Incestraja03_1390500309328273408(270P).mp4", "rb"), supports_streaming=True)
    await bot.stend_video(chat_id=message.chat_id, video=open("Incestraja03_1391614944739684359(320P).mp4", "rb"), supports_streaming=True)
    await bot.stend_video(chat_id=message.chat_id, video=open("Incestraja03_1393868271972020225(320P)).mp4", "rb"), supports_streaming=True)
    await bot.stend_video(chat_id=message.chat_id, video=open("Incestraja03_1403664652073005058(270P).mp4", "rb"), supports_streaming=True)
    await bot.stend_video(chat_id=message.chat_id, video=open("Incestraja03_1403664652073005058(270P).mp4", "rb"), supports_streaming=True)"""

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
