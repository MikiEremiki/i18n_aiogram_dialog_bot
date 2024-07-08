from typing import Dict, List

from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text
from fluentogram import TranslatorRunner


class I18NFormat(Text):
    def __init__(self, text: str,
                 list_keys: List[str] | None = None,
                 when: WhenCondition = None):
        super().__init__(when)
        self.text = text
        self.list_keys = list_keys

    async def _render_text(self, data: Dict, manager: DialogManager) -> str:
        i18n: TranslatorRunner = manager.middleware_data.get('i18n')
        return i18n.get(self.text, **data)
