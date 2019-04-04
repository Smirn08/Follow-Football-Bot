from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
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


# def greet_user(bot, update):
#     emo_hi = emojize(choice(settings.USER_EMOJI), use_aliases=True)
#     text = '''Привет {} {}, давай смотреть футбол вместе!
# Подписывайся на свой любимый клуб и ты никогда не пропустишь матч!
# Какой твой любимый клуб EPL?'''.format(update.message.chat.first_name, emo_hi)
#     my_keyboard = ReplyKeyboardMarkup(settings.MAIN_KEYS)
#     update.message.reply_text(f'{text}', reply_markup=my_keyboard)


def talk_to_me(bot, update):
    user_text = 'Хей, {}, я пока не знаю почему ты написал "{}", но скоро ' \
        'узнаю!'.format(update.message.chat.first_name, update.message.text)
    print(user_text)
    update.message.reply_text(user_text)


def start(bot, update):
    emo_hi = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    text = '''Привет {} {}, давай смотреть футбол вместе!
Подписывайся на свой любимый клуб и ты никогда не пропустишь матч!
Какой твой любимый клуб EPL?'''.format(update.message.chat.first_name, emo_hi)
    update.message.reply_text(text, reply_markup=start_keyboard())


def start_keyboard():
    keyboard = [[InlineKeyboardButton('Выбрать клуб', callback_data='p1')]]
    return InlineKeyboardMarkup(keyboard)


def first_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                    message_id=query.message.message_id,
                    text=settings.LIST_ONE,
                    reply_markup=first_page_keyboard(),
                    parse_mode='Markdown')


def first_page_keyboard():
    keyboard = [[InlineKeyboardButton('>', callback_data='p2')]]
    return InlineKeyboardMarkup(keyboard)


def second_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                    message_id=query.message.message_id,
                    text=settings.LIST_TWO,
                    reply_markup=second_page_keyboard(),
                    parse_mode='Markdown')


def second_page_keyboard():
    keyboard = [[InlineKeyboardButton('|<', callback_data='p1'),
                InlineKeyboardButton('>', callback_data='p3')]]
    return InlineKeyboardMarkup(keyboard)


def third_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                    message_id=query.message.message_id,
                    text=settings.LIST_THREE,
                    reply_markup=third_page_keyboard(),
                    parse_mode='Markdown')


def third_page_keyboard():
    keyboard = [[InlineKeyboardButton('<', callback_data='p2'),
                InlineKeyboardButton('>|', callback_data='p4')]]
    return InlineKeyboardMarkup(keyboard)


def forth_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                    message_id=query.message.message_id,
                    text=settings.LIST_FOUR,
                    reply_markup=forth_page_keyboard(),
                    parse_mode='Markdown')


def forth_page_keyboard():
    keyboard = [[InlineKeyboardButton('<', callback_data='p3')]]
    return InlineKeyboardMarkup(keyboard)


###############################################################################


def my_club(bot, update):
    chat_id = update.message.chat_id
    club = update.message.text
    if club == '/afcb':
        t_info = take_club_from_db(1)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/afc':
        t_info = take_club_from_db(2)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/bha':
        t_info = take_club_from_db(3)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/bfc':
        t_info = take_club_from_db(4)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/car':
        t_info = take_club_from_db(5)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/cfc':
        t_info = take_club_from_db(6)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/cpfc':
        t_info = take_club_from_db(7)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/efc':
        t_info = take_club_from_db(8)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/ffc':
        t_info = take_club_from_db(9)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/htfc':
        t_info = take_club_from_db(10)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/lei':
        t_info = take_club_from_db(11)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/lfc':
        t_info = take_club_from_db(12)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/mcfc':
        t_info = take_club_from_db(13)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/mufc':
        t_info = take_club_from_db(14)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/new':
        t_info = take_club_from_db(15)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/sou':
        t_info = take_club_from_db(16)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/tot':
        t_info = take_club_from_db(17)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/wfc':
        t_info = take_club_from_db(18)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/whu':
        t_info = take_club_from_db(19)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    elif club == '/wol':
        t_info = take_club_from_db(20)
        logo_link = t_info[12]
        bot.send_photo(chat_id=chat_id, photo=logo_link,
        caption=f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                   .replace('https://','')}]({t_info[13]})''',
        parse_mode="Markdown")
    else:
        update.message.reply_text('Такого клуба нет в EPL')


###############################################################################

def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher

    for club in settings.CLUB_COMMAND_LIST:
        dp.add_handler(CommandHandler(club, my_club))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(first_page, pattern='p1'))
    dp.add_handler(CallbackQueryHandler(second_page, pattern='p2'))
    dp.add_handler(CallbackQueryHandler(third_page, pattern='p3'))
    dp.add_handler(CallbackQueryHandler(forth_page, pattern='p4'))


    mybot.start_polling()
    mybot.idle()


main()
