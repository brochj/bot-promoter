# -*- coding: utf-8 -*-

class Actions:
    def __init__(self, api):
        self.api = api

    def tweet(self, text: str):
        return self.api.update_status(text)

    def reply(self, text: str, in_reply_to_status_id: int):
        return self.api.update_status(text, in_reply_to_status_id=in_reply_to_status_id)
