import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in .env file")
from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.quiz import router as quiz_router, handle_open_answer
from handlers.goals import router as goals_router
from handlers.pets import router as pets_router
from handlers.profile import router as profile_router
from handlers.help import router as help_router
from handlers.feedback import router as feedback_router, handle_feedback_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Catch-all router — must be registered LAST
fallback_router = Router()


@fallback_router.message()
async def catch_all_messages(message: Message) -> None:
    """Catch-all: check open-ended quiz answer, then feedback, otherwise ignore."""
    if message.text:
        if await handle_open_answer(message):
            return
        if await handle_feedback_message(message):
            return


# Register routers (order matters)
dp.include_router(start_router)
dp.include_router(quiz_router)
dp.include_router(help_router)
dp.include_router(feedback_router)
dp.include_router(goals_router)
dp.include_router(pets_router)
dp.include_router(profile_router)
dp.include_router(menu_router)
dp.include_router(fallback_router)


async def main() -> None:
    logger.info("Bot starting...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
