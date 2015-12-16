"""
Telegram Bot created to deliver secret santa clues and riddles to
Olga Karavayeva.
"""
import asyncio
import datetime
import json
import logging
import random
import sys

import telepot
from telepot.async.delegate import create_open
from telepot.delegate import per_chat_id

from clues import CLUES

logging.basicConfig(filename='messages.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class SecretSantaBot(telepot.helper.ChatHandler):
    """Bot class to handle clues, riddles and answers."""

    help_text = """You can control me by sending these commands:

/answer - give a possible answer to the current clue
/current - shows the current clue
/random - give you some random answers :)
/help - shows help
"""
    log = []
    texts_log = []

    def __init__(self, seed_tuple, timeout):
        super(SecretSantaBot, self).__init__(seed_tuple, timeout)
        self.clues = CLUES
        self._solved_clues = []
        self._current_command = None
        self._fails = 0
        self._solved = False
        self._set_current_clue(1)

    @staticmethod
    def _build_message(answer):
        if isinstance(answer, tuple):
            return answer
        return "text", answer

    @staticmethod
    def _get_random_answer():
        random_files = ["files/random/random%s.gif" % i for i in range(1, 8)]
        return "document", {"file": random.choice(random_files)}

    @staticmethod
    def _is_clue_available(clue):
        available = clue.get("available", True)
        if isinstance(available, datetime.date):
            today = datetime.date.today()
            return today >= available
        return available

    def _set_current_clue(self, index):
        self._current_unsolved_clue_index = index
        self._current_unsolved_clue_key = "clue-%s" % index

    def _get_current_clue(self):
        return self.clues[self._current_unsolved_clue_key]

    def current_clue_message(self):
        """Gets the current unsolved question."""
        try:
            return self._build_message(self._get_current_clue()["question"])
        except KeyError:
            return "text", "Ups, there's no clue right now! Try again tomorrow, sorry!"

    def check_answer(self, msg):
        """Checks the answer given.
        :param msg:
        """
        self._current_command = None
        clue = self._get_current_clue()
        if not self._is_clue_available(clue):
            return "text", "Ups, there's no clue right now! Try again tomorrow, sorry!"
        message = self._build_message(clue["answers"]["wrong"])
        kind = message[0]
        wrong = message[1]
        content_type, chat_type, chat_id = telepot.glance2(msg)
        if content_type == "text":
            answer = msg["text"].strip().lower()
            if answer in clue["solutions"]:
                self._fails = 0
                self._set_current_clue(self._current_unsolved_clue_index + 1)
                self._solved = clue.get("solve", False)
                return self._build_message(clue["answers"]["correct"])
        self._fails += 1
        if self._fails > random.randint(4, 8) and clue["hints"]:
            return "text", "Wrong! Some extra clue: %s" % random.choice(clue["hints"])
        return kind, wrong

    def analyze_message(self, msg):
        """Analyze commands on the message and gets the proper answers.
        :param msg:
        """
        self.log.append(json.dumps(msg))
        answer = ("text", "I don't understand what are you saying, sorry!")
        content_type, chat_type, chat_id = telepot.glance2(msg)
        if content_type == "text":
            self.texts_log.append(msg["text"])
            command = msg['text'].strip().lower().split(' ')[0]
            # Save current command
            if command[0] == '/':
                self._current_command = command
            # Execute current command
            if command == '/help':
                answer = ("text", self.help_text)
            elif command == "/start":
                answer = ("text", """Hi Olga!
Welcome to you Secret Santa Bot! I'll give you some questions/riddles that will give you some clues about myself. \
Every time you give me a correct answer, I'll give you a new question/riddle, easy!

%s
""" % self.help_text)
            elif command == "/random":
                answer = self._get_random_answer()
            elif command == "/current":
                clue = self._get_current_clue()
                if not self._is_clue_available(clue):
                    answer = ("text", "Ups, there's no clue right now! Try again tomorrow, sorry!")
                else:
                    answer = self.current_clue_message()
            elif command == "/answer":
                clue = self._get_current_clue()
                if not self._is_clue_available(clue):
                    answer = ("text", "Ups, there's no clue right now! Try again tomorrow, sorry!")
                else:
                    answer = ("text", "So, what's you answer?")
            elif command == "/log":
                answer = ("text", "\n".join(self.log))
            elif command == "/texts_log":
                answer = ("text", "\n".join(self.texts_log))
            elif command[0] != "/":
                if self._current_command == "/answer":
                    answer = self.check_answer(msg)
                else:
                    if random.randint(1, 100) > 15:
                        answer = ("text", """
Do you hope I'll give you some extra information for free? Not on my watch!

If you want to give an answer, you should enter /answer command first :)
""")
                    else:
                        answer = ("document", {"text": "You should enter /answer first!", "file": "files/extra1.gif"})
        return answer

    @asyncio.coroutine
    def open(self, initial_msg, seed):
        logger.info(json.dumps(initial_msg))
        full_answer = self.analyze_message(initial_msg)
        kind = full_answer[0]
        answer = full_answer[1]
        if kind == "text":
            yield from self.sender.sendMessage(answer)
        elif kind == "photo" and isinstance(answer, dict):
            with open(answer["file"], "r") as photo_file:
                yield from self.sender.sendPhoto(photo_file, caption=answer.get("caption", ""))
        return True

    @asyncio.coroutine
    def on_message(self, msg):
        logger.info(json.dumps(msg))
        full_answer = self.analyze_message(msg)
        kind = full_answer[0]
        answer = full_answer[1]
        if kind == "text":
            yield from self.sender.sendMessage(answer)
        elif kind == "photo" and isinstance(answer, dict):
            with open(answer["file"], "rb") as media_file:
                yield from self.sender.sendPhoto(media_file, caption=answer.get("caption", ""))
        elif kind == "video" and isinstance(answer, dict):
            yield from self.sender.sendMessage("Wait for it...")
            with open(answer["file"], "rb") as media_file:
                yield from self.sender.sendVideo(media_file, caption=answer.get("caption", ""))
        elif kind == "document" and isinstance(answer, dict):
            yield from self.sender.sendMessage("Wait for it...")
            with open(answer["file"], "rb") as media_file:
                yield from self.sender.sendDocument(media_file)
                text = answer.get("text", "")
                if text:
                    yield from self.sender.sendMessage(text)
        elif kind == "sticker":
            yield from self.sender.sendSticker(answer)
        elif kind == "audio" and isinstance(answer, dict):
            yield from self.sender.sendMessage("Wait for it...")
            with open(answer["file"], "rb") as media_file:
                text = answer.get("text", "")
                if text:
                    yield from self.sender.sendMessage(text)
                yield from self.sender.sendAudio(media_file, title=answer.get("text", ""))

    @asyncio.coroutine
    def on_close(self, exception):
        if isinstance(exception, telepot.helper.WaitTooLong):
            yield from self.sender.sendMessage("Good bye!")


if __name__ == "__main__":
    # We get the token from command line...
    TOKEN = sys.argv[1]
    # Creates the bot and the event loop...
    bot = telepot.async.DelegatorBot(TOKEN, [
        (per_chat_id(), create_open(SecretSantaBot, timeout=604800)),
    ])
    loop = asyncio.get_event_loop()
    loop.create_task(bot.messageLoop())
    print('Listening ...')
    loop.run_forever()
