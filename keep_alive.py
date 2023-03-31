from flask import Flask
from threading import Thread
import logging

app = Flask('')

@app.route('/')
def home(): 
  return "Bot is connecting.."

'''
def admin():
  code=1776
  if code == 1776:
    text = input("Enter the message :")
    id = int(input("chat id who you want to send :"))
'''

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()