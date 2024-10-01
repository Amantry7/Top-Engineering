from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked
from django.conf import settings

# Telegram Bot settings

async def send_telegram_message(message):
    try:
        bot = Bot(token=settings.TELEGRAM_TOKEN)
        await bot.send_message(settings.GROUP_ID, message)
    except BotBlocked:
        print("Bot is blocked by the user or group.")
