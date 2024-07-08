from aiogram import html
from aiogram.types import User, CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button
from fluentogram import TranslatorRunner

from custom_widgets.i18n_format import I18NFormat
from states import states


async def get_user(
        event_from_user: User,
        **kwargs,
) -> dict[str, str]:
    username = html.quote(event_from_user.full_name)
    return {'username': username}


async def button_click(
        callback: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await callback.answer(text=i18n.get('button-pressed'))


start_dialog = Dialog(
    Window(
        I18NFormat('hello-user', ['username']),
        Button(I18NFormat('button-button'),
               id='button_pressed',
               on_click=button_click),
        getter=get_user,
        state=states.Main.START,
    ),
)
