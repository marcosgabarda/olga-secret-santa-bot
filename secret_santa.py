"""
Telegram Bot created to deliver secret santa clues and riddles to
Olga Karavayeva.
"""
import asyncio
import sys

import telepot
import telepot.async
from telepot.delegate import per_chat_id, create_open


class SecretSantaBot(telepot.helper.ChatHandler):

    def __init__(self, seed_tuple, timeout):
        super(SecretSantaBot, self).__init__(seed_tuple, timeout)

    @asyncio.coroutine
    def on_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        print(content_type, chat_type, chat_id)
        yield from self.sender.sendMessage("cool!")

if __name__ == "__main__":

    TOKEN = sys.argv[1]

    bot = telepot.async.DelegatorBot(TOKEN, [
        (per_chat_id(), create_open(SecretSantaBot, timeout=10)),
    ])
    loop = asyncio.get_event_loop()
    loop.create_task(bot.messageLoop())
    print('Listening ...')
    loop.run_forever()
