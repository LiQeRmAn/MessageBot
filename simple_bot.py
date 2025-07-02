from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

import os
from dotenv import load_dotenv
load_dotenv()  # Загрузка переменных сред из .env-файла

TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я простой бот.")

async def echo_message(update: Update, context):
    user_message = update.message.text
    response = f"Я получил сообщение '{user_message}'"
    await update.message.reply_text(response)

if __name__ == '__main__':
    # Подключаемся к серверу Telegram
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Обработчик команды /start
    application.add_handler(CommandHandler('start', start))
    
    # Обработчик всех остальных сообщений
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo_message))
    
    print("Бот запущен...")
    application.run_polling()