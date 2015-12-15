"""
Telegram Bot created to deliver secret santa clues and riddles to
Olga Karavayeva.
"""
import asyncio
import json
import logging
import sys

import telepot
from telepot.async.delegate import create_open
from telepot.delegate import per_chat_id

logger = logging.getLogger(__name__)


class SecretSantaBot(telepot.helper.ChatHandler):
    """Bot class to handle clues, riddles and answers."""

    clues = {
        "clue-1": {
            "question": "How says a snake 'hello' to everyone?",
            "solutions": ("print('hello world')", 'print("hello world")'),
            "answers": {
                "correct": "Great! You have one! :D",
                "wrong": "Ups, that's not the answer you're looking for",
            }
        }
    }

    help_text = """You can control me by sending these commands:

/answer - give a possible answer to the current clue
/current - shows the current clue
"""
    log = []
    texts_log = []

    def __init__(self, seed_tuple, timeout):
        super(SecretSantaBot, self).__init__(seed_tuple, timeout)
        self._solved_clues = []
        self._current_unsolved_clue_index = 1
        self._current_unsolved_clue_key = "clue-1"
        self._current_command = None

    def _get_current_clue(self):
        return self.clues[self._current_unsolved_clue_key]

    def current_clue_message(self):
        """Gets the current unsolved question."""
        try:
            return self._get_current_clue()["question"]
        except KeyError:
            return "Ups, there's no clue right now! Try again later, sorry!"

    def check_answer(self, msg):
        """Checks the answer given.
        :param msg:
        """
        self._current_command = None
        clue = self._get_current_clue()
        kind, wrong = "text", clue["answers"]["wrong"]
        content_type, chat_type, chat_id = telepot.glance2(msg)
        if content_type == "text":
            answer = msg["text"].strip().lower()
            if answer in clue["solutions"]:
                self._current_unsolved_clue_index += 1
                self._current_unsolved_clue_key = "clue-%s" % self._current_unsolved_clue_index
                return "text", clue["answers"]["correct"]
        return kind, wrong

    def analyze_message(self, msg):
        """Analyze commands on the message and gets the proper answers.
        :param msg:
        """
        self.log.append(json.dumps(msg))
        kind, answer = "text", "I don't understand what are you saying, sorry!"
        content_type, chat_type, chat_id = telepot.glance2(msg)
        if content_type == "text":
            self.texts_log.append(msg["text"])
            command = msg['text'].strip().lower().split(' ')[0]
            # Save current command
            if command[0] == '/':
                self._current_command = command
            # Execute current command
            if command == '/help':
                answer = self.help_text
            elif command == "/start":
                answer = """Hi Olga!
Welcome to you Secret Santa Bot! I'll give you some questions/riddles that will give you some clues about myself. Every time you give me a correct answer, I'll give you a new question/riddle, easy!

%s
""" % self.help_text
            elif command == "/current":
                answer = self.current_clue_message()
            elif command == "/answer":
                answer = "So, what's you answer?"
            elif command == "/log":
                answer = "\n".join(self.log)
            elif command == "/texts_log":
                answer = "\n".join(self.texts_log)
            elif command[0] != "/":
                if self._current_command == "/answer":
                    kind, answer = self.check_answer(msg)
                else:
                    answer = "Do you hope I'll give you some extra information for free? Not on my watch!"
        return kind, answer

    @asyncio.coroutine
    def open(self, initial_msg, seed):
        logger.debug(json.dumps(initial_msg))
        kind, answer = self.analyze_message(initial_msg)
        if kind == "text":
            yield from self.sender.sendMessage(answer)
        return True

    @asyncio.coroutine
    def on_message(self, msg):
        logger.debug(json.dumps(msg))
        kind, answer = self.analyze_message(msg)
        if kind == "text":
            yield from self.sender.sendMessage(answer)

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
