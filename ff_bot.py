import logging
from random import choice

import settings
from my_bot_token import TOKEN
from my_bot_proxy import PROXY
from take_club_from_db import take_club_from_db
from check_user import check_user_in_db
from check_user import add_user
from check_user import take_club_id

from emoji import emojize

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import CallbackQueryHandler, ConversationHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler('bot.log', 'w', 'utf-8')]
                    )


def talk_to_me(bot, update):
    user_text = 'Хей, {}, я пока не знаю почему ты написал "{}", но скоро ' \
        'узнаю!'.format(update.message.chat.first_name, update.message.text)
    print(user_text)
    update.message.reply_text(user_text)


def start(bot, update):
    chat_id = update.message.chat_id
    status = check_user_in_db(chat_id)
    if status is True:
        main_menu(bot, update)
    if status is False:
        emo_hi = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        text = '''Привет *{}* {}, давай смотреть футбол вместе!
Подписывайся на свой любимый клуб и ты никогда не пропустишь матч!
Какой твой любимый клуб EPL?'''.format(update.message.chat.first_name, emo_hi)
        update.message.reply_text(
            text, reply_markup=InlineKeyboardMarkup(settings.START_KEYS),
            parse_mode='Markdown')


def first_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_ONE,
        reply_markup=InlineKeyboardMarkup(settings.FIRST_PAGE_KEYS),
        parse_mode='Markdown',
        )


def second_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_TWO,
        reply_markup=InlineKeyboardMarkup(settings.SECOND_PAGE_KEYS),
        parse_mode='Markdown',
        )


def third_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_THREE,
        reply_markup=InlineKeyboardMarkup(settings.THIRD_PAGE_KEYS),
        parse_mode='Markdown',
        )


def forth_page(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_FOUR,
        reply_markup=InlineKeyboardMarkup(settings.FORTH_PAGE_KEYS),
        parse_mode='Markdown',
        )


def my_club(bot, update):
    chat_id = update.message.chat_id
    bot.delete_message(chat_id=chat_id,
         message_id=update.message.message_id)
    if update.message.text in settings.CLUBS_TG_ID.keys():
        club_db_id = settings.CLUBS_TG_ID[update.message.text]
        t_info = take_club_from_db(club_db_id)
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
        reply_markup=InlineKeyboardMarkup(settings.LAST_CHOICE),
        parse_mode="Markdown")
        add_user(chat_id, club_db_id)


def add_user_in_db(bot, update):
    query = update.callback_query
    bot.delete_message(chat_id=query.message.chat_id,
        message_id=query.message.message_id)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f"Я запомнил твой выбор",
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown',
        )


def change_club(bot, update):
    query = update.callback_query
    bot.delete_message(chat_id=query.message.chat_id,
        message_id=query.message.message_id)
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f"Решил выбрать другой клуб?",
        reply_markup=InlineKeyboardMarkup(settings.CHANGE_CLUB),
        parse_mode='Markdown',
        )


def main_menu(bot, update):
    try:
        query = update.callback_query
        bot.delete_message(chat_id=query.message.chat_id,
            message_id=query.message.message_id)
        bot.send_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            text=f">>>>>>>>>>>> *ОСНОВНОЕ МЕНЮ* <<<<<<<<",
            reply_markup=InlineKeyboardMarkup(settings.MAIN_MENU_KEYS),
            parse_mode='Markdown',
            )
    except AttributeError:
        chat_id = update.message.chat_id
        bot.send_message(
            chat_id=chat_id,
            message_id=update.message.message_id,
            text=f">>>>>>>>>>>> *ОСНОВНОЕ МЕНЮ* <<<<<<<<",
            reply_markup=InlineKeyboardMarkup(settings.MAIN_MENU_KEYS),
            parse_mode='Markdown',
            )


def match_links(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'''Команда 1 - Команда 2
АПЛ | 33-й тур | Начало в 22:00 МСК

✔️*SopCast:*
sop://broker.sopcast.com:3912/256999 (2000kbps)
...

✔️*Трансляции онлайн:*
▶️https://vk.cc/9ghs3y
▶️https://vk.cc/9ghsac

✔️*Ace Stream:*
acestream://d518402ca40430db6107a777879b511e9b930817 (1500kbps)
...''',
        reply_markup=InlineKeyboardMarkup(settings.LINKS),
        parse_mode='Markdown',
        )


def alarm(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'''ТУТ БУДЕТ ВОЗМОЖНОСТЬ НАСТРОИТЬ УВЕДОМЛЕНИЯ''',
        reply_markup=InlineKeyboardMarkup(settings.ALARM),
        parse_mode='Markdown',
        )


def next_match(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'*Следующий матч:* Slavia Praha - Chelsea FC | 11/04/2019	в 20:00',
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown',
        )


def last_match(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'*Прошедший матч:* Chelsea FC - West Ham United | *2:0*',
        reply_markup=InlineKeyboardMarkup(settings.LAST_GAME),
        parse_mode='Markdown',
        )


def last_match_more(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'''ПОДРОБНАЯ ИНФОРМАЦИЯ О МАТЧЕ''',
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown',
        )


def current_table(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'[Текущая таблица](http://www.espn.com/soccer/standings/_/league/eng.1)',
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown',
        )


def my_club_info(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    bot.delete_message(chat_id=chat_id,
        message_id=query.message.message_id)
    print(query.message.message_id)

    club_db_id = take_club_id(439051112)  # необходимо пофиксить, чтоб выводил клуб юзера, не могу понять как получить id юзера
    t_info = take_club_from_db(club_db_id)
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
    reply_markup=InlineKeyboardMarkup(settings.MY_CLUB_MENU),
    parse_mode="Markdown")


def about_me(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.ABOUT,
        reply_markup=InlineKeyboardMarkup(settings.ABOUT_BUTTONS),
        parse_mode='Markdown',
        )


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher

    for club in settings.CLUB_COMMAND_LIST:
        dp.add_handler(CommandHandler(club, my_club))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('menu', main_menu))
    dp.add_handler(CommandHandler('my_club', my_club_info))
    dp.add_handler(CallbackQueryHandler(first_page, pattern='p1'))
    dp.add_handler(CallbackQueryHandler(second_page, pattern='p2'))
    dp.add_handler(CallbackQueryHandler(third_page, pattern='p3'))
    dp.add_handler(CallbackQueryHandler(forth_page, pattern='p4'))
    dp.add_handler(CallbackQueryHandler(add_user_in_db, pattern='add_user'))
    dp.add_handler(CallbackQueryHandler(change_club, pattern='change'))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='menu'))
    dp.add_handler(CallbackQueryHandler(match_links, pattern='links'))
    dp.add_handler(CallbackQueryHandler(next_match, pattern='next'))
    dp.add_handler(CallbackQueryHandler(last_match, pattern='last'))
    dp.add_handler(CallbackQueryHandler(current_table, pattern='table'))
    dp.add_handler(CallbackQueryHandler(my_club_info, pattern='my_club'))
    dp.add_handler(CallbackQueryHandler(about_me, pattern='about'))
    dp.add_handler(CallbackQueryHandler(last_match_more, pattern='game'))
    dp.add_handler(CallbackQueryHandler(alarm, pattern='alarm'))


    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
