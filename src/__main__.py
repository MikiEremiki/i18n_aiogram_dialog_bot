import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from config_data.config import Config, load_config
from dialogs.start import start_dialog
from handlers.commands import commands_router
from handlers.other import other_router
from middlewares.i18n_middlewares import TranslatorRunnerMiddleware
from utils.i18n_translator_nub import create_translator_hub

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(commands_router)
    dp.include_router(other_router)
    dp.include_router(start_dialog)

    translator_hub: TranslatorHub = create_translator_hub()
    dp.update.middleware(TranslatorRunnerMiddleware(translator_hub))

    setup_dialogs(dp)
    await dp.start_polling(bot)


asyncio.run(main())
