from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from states import states

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
        message: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(state=states.Main.START,
                               mode=StartMode.RESET_STACK)
    