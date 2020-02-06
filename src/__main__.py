import logging

from src.bot.bot import Bot

logger = logging.getLogger()


def main():
    bot = Bot()
    bot.start()


if __name__ == '__main__':
    main()
