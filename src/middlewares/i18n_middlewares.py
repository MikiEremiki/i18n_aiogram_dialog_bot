from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub


class TranslatorRunnerMiddleware(BaseMiddleware):
    def __init__(
            self,
            hub: TranslatorHub,
            default_lang: str = 'ru',
    ):
        super().__init__()
        self.hub = hub
        self.default_lang = default_lang

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        user: User | None = data.get('event_from_user', None)

        if user is None:
            locale = self.default_lang
        else:
            locale = user.language_code
        data['i18n'] = self.hub.get_translator_by_locale(locale=locale)

        return await handler(event, data)
