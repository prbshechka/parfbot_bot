from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Встановлюємо логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привіт! Я твій бот. Як справи?')

# Обробка повідомлень
async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    await update.message.reply_text(f'Ти сказав: {user_message}')

# Основна функція
def main() -> None:
    # Встав свій токен
    token = "7792220190:AAESX75d2zclIR2zy9LbMw78-QnJcWuBaB8"

    # Створюємо Application
    application = Application.builder().token(token).build()

    # Реєструємо обробники команд
    application.add_handler(CommandHandler("start", start))

    # Реєструємо обробник повідомлень
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаємо бота
    application.run_polling()

if __name__ == '__main__':
    main()
