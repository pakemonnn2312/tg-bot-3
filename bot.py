
import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Load .env
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is not set in .env file")

# Init bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# /start handler
@router.message(CommandStart())
async def start_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Переглянути приклади📸")],
            [KeyboardButton(text="Про нас"), KeyboardButton(text="Контакти📞")],
        ],
        resize_keyboard=True,
    )
    await message.answer(
        "👋 Вітаємо Вас у нашому боті!\n"
        "🏗️ Ми спеціалізуємось на виготовленні та встановленні бетонних огорож у Білоцерківському районі.\n"
        "🔨 Працюємо вже понад 10 років, тому добре знаємо свою справу та гарантуємо якість і надійність",
        reply_markup=keyboard,
    )

@router.message(F.text == "Переглянути приклади📸")
async def show_examples(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="📷 Переглянути приклади робіт",
                url="https://photos.app.goo.gl/1KzH9n9EnSGQjJrJ9"
            )]
        ]
    )
    await message.answer(
        "🔍 Хочете побачити, як виглядає результат нашої роботи?\n"
        "Перегляньте реальні фото встановлених бетонних огорож 👇",
        reply_markup=keyboard
    )

@router.message(F.text == "Про нас")
async def about_us(message: Message):
    await message.answer(
        "🏗️ <b>Про нас</b>\n\n"
        "Наша команда вже понад 10 років займається виготовленням та встановленням бетонних огорож. "
        "За цей час ми реалізували десятки проєктів у Київській області, зокрема в місті Тараща та навколишніх селах.\n\n"
        "<b>Ми пропонуємо:</b>\n"
        "✅ Якісні бетонні секції власного виробництва\n"
        "✅ Надійний монтаж з дотриманням усіх стандартів\n"
        "✅ Індивідуальний підхід до кожного клієнта\n"
        "✅ Вчасне виконання замовлень\n\n"
        "🔨 Ми впевнені в якості нашої роботи, адже самі виготовляємо продукцію та контролюємо кожен етап — від виробництва до встановлення.\n\n"
        "<b>Обираючи нас, ви отримуєте:</b>\n"
        "💪 Досвід, перевірений роками\n"
        "📈 Гарантію на довговічність\n"
        "☎️ Швидкий зв’язок і консультацію\n\n"
        "Ми цінуємо довіру кожного клієнта і завжди працюємо на результат!",
        parse_mode="HTML"
    )

@router.message(F.text == "Контакти📞")
async def contact(message: Message):
    await message.answer(
        "📞 <b>Контакти для замовлення</b>:\n+38 (098) 227‑48‑80📲\nТелефонуйте прямо зараз!",
        parse_mode="HTML"
    )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
