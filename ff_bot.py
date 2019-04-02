from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from random import choice
from emoji import emojize
from my_bot_token import TOKEN
from my_bot_proxy import PROXY
from take_club_from_db import take_club_from_db
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


def club_follow(bot, update):
    club = update.message.text.split()[1]
    if club == 'afc_b':
        update.message.reply_text(take_club_from_db(1))
    elif club == 'ars':
        update.message.reply_text(take_club_from_db(2))
    elif club == 'bri':
        update.message.reply_text(take_club_from_db(3))
    elif club == 'burn':
        update.message.reply_text(take_club_from_db(4))
    elif club == 'card':
        update.message.reply_text(take_club_from_db(5))
    elif club == 'cfc':
        update.message.reply_text(take_club_from_db(6))
    elif club == 'cry':
        update.message.reply_text(take_club_from_db(7))
    elif club == 'eve':
        update.message.reply_text(take_club_from_db(8))
    elif club == 'ful':
        update.message.reply_text(take_club_from_db(9))
    elif club == 'hud':
        update.message.reply_text(take_club_from_db(10))
    elif club == 'lei':
        update.message.reply_text(take_club_from_db(11))
    elif club == 'lfc':
        update.message.reply_text(take_club_from_db(12))
    elif club == 'city':
        update.message.reply_text(take_club_from_db(13))
    elif club == 'mnu':
        update.message.reply_text(take_club_from_db(14))
    elif club == 'new':
        update.message.reply_text(take_club_from_db(15))
    elif club == 'sou':
        update.message.reply_text(take_club_from_db(16))
    elif club == 'tot':
        update.message.reply_text(take_club_from_db(17))
    elif club == 'wat':
        update.message.reply_text(take_club_from_db(18))
    elif club == 'whu':
        update.message.reply_text(take_club_from_db(19))
    elif club == 'wol':
        update.message.reply_text(take_club_from_db(20))
    else:
        update.message.reply_text('Такого клуба нет в EPL')


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('club', club_follow))

    mybot.start_polling()
    mybot.idle()


main()
