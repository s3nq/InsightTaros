# bot.py

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, APP_URL

# Выводим токен для проверки (только для отладки, не оставляй в финальном коде)
print(f"BOT_TOKEN: {BOT_TOKEN}")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    keyboard = [
        [
            InlineKeyboardButton(
                text="Начать гадание на Таро",
                web_app={'url': APP_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Привет, {user.first_name}! Добро пожаловать в TarotBot 🔮.\n"
        "Нажми на кнопку ниже, чтобы начать гадание.",
        reply_markup=reply_markup
    )

# Главная функция запуска бота
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    # Запуск бота с polling (для локального тестирования)
    application.run_polling()

if __name__ == '__main__':
    main()