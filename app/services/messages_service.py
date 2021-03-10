import random

from app.services.messages import good_messages, bad_messages


class MessageService:
    def get_good_vibe_message(self):
        good_vibe = random.choice(good_messages)
        return good_vibe

    def get_bad_vibe_message(self):
        bad_vibe = random.choice(bad_messages)
        return bad_vibe
