"""
Telegram Bot created to deliver secret santa clues and riddles to
Olga Karavayeva.
"""
import telepot


class SecretSantaBot(telepot.Bot):

    # TOKEN = "163681199:AAHYK1acri1hAUnnLPw1tl2gSON7fAWwfRY"
    # def __init__(self):
    #     self.bot = telepot.Bot(TOKEN)
    #     me = self.bot.getMe()
    #     for key, value in me.items():
    #         setattr(self, key, value)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance2(msg)
        print(content_type, chat_type, chat_id)

    def run(self):
        self.bot.notifyOnMessage(run_forever=True)
        print("Listening ...")
        while True:
            time.sleep(10)

if __name__ == "__main__":

    secret_santa_bot = SecretSantaBot()
