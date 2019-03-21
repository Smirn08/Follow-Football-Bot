from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from random import choice
from emoji import emojize
from my_bot_token import TOKEN
from my_bot_proxy import PROXY
import settings
import logging


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler('bot.log', 'w', 'utf-8')]
                    )


def greet_user(bot, update):
    emo_hi = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    text = '''Привет {} {}, давай смотреть футбол вместе!
Подписывайся на свой любимый клуб и ты никогда не пропустишь матч!
Какой твой любимый клуб EPL?'''.format(update.message.chat.first_name, emo_hi)
    my_keyboard = ReplyKeyboardMarkup(settings.MAIN_KEYS)
    update.message.reply_text(f'{text}', reply_markup=my_keyboard)


def talk_to_me(bot, update):
    user_text = 'Хей, {}, я пока не знаю почему ты написал "{}", но скоро ' \
        'узнаю!'.format(update.message.chat.first_name, update.message.text)
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
