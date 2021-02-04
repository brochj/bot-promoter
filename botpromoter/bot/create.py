# -*- coding: utf-8 -*-

from bot.actions import Actions
from bot.search import Search


class CreateBot:
    def __init__(self, api, config=None):
        # dependency injection
        # Se não for passado um config (nova dependência)
        # vai ser o padrão ->  Actions() e Search()
        try:
            self.actions = config.actions
        except AttributeError:
            self.actions = Actions(api)

        try:
            self.search = config.search
        except AttributeError:
            self.search = Search(api)
