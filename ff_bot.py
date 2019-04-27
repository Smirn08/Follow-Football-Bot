import logging
from random import choice

import settings
import bot_user
import ten_matches
import stream_links
from my_bot_token import TOKEN
from my_bot_proxy import PROXY
from take_club_from_db import take_club_from_db

from emoji import emojize

from telegram import InlineKeyboardMarkup

from telegram.ext import CallbackQueryHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler('bot.log', 'w', 'utf-8')]
)


def clean(bot, update):
    # удаляет вест флуд пользователя
    chat_id = update.message.chat_id
    bot.delete_message(
        chat_id=chat_id, message_id=update.message.message_id
    )
    print(update.message.text)


def start(bot, update):
    # приветствие нового пользователя
    chat_id = update.message.chat_id
    status = bot_user.check_in_db(chat_id)
    if status is True:
        main_menu(bot, update)
    if status is False:
        emo_hi = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        text = '''Привет *{}* {}, давай смотреть футбол вместе!
Подписывайся на свой любимый клуб и ты никогда не пропустишь матч!
Какой твой любимый клуб EPL?'''.format(update.message.chat.first_name, emo_hi)
        update.message.reply_text(
            text, reply_markup=InlineKeyboardMarkup(settings.START_KEYS),
            parse_mode='Markdown'
        )


def first_page(bot, update):
    # первая страница со списком клубов EPL
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_ONE,
        reply_markup=InlineKeyboardMarkup(settings.FIRST_PAGE_KEYS),
        parse_mode='Markdown'
    )
    # запись Id сообщения в переменную, чтоб можно было потом удалить
    settings.QUERY_ID = query.message.message_id


def second_page(bot, update):
    # вторая страница со списком клубов EPL
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_TWO,
        reply_markup=InlineKeyboardMarkup(settings.SECOND_PAGE_KEYS),
        parse_mode='Markdown'
    )


def third_page(bot, update):
    # третья страница со списком клубов EPL
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_THREE,
        reply_markup=InlineKeyboardMarkup(settings.THIRD_PAGE_KEYS),
        parse_mode='Markdown'
    )


def forth_page(bot, update):
    # четвертая страница со списком клубов EPL
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.LIST_FOUR,
        reply_markup=InlineKeyboardMarkup(settings.FORTH_PAGE_KEYS),
        parse_mode='Markdown'
    )


def my_club(bot, update):
    # блок представления клуба, который выбирает пользователь ДО МЕНЮ
    chat_id = update.message.chat_id
    fn = update.message.from_user['first_name']
    ln = update.message.from_user['last_name']
    tg_fullname = f'{fn} {ln}'
    tg_nickname = update.message.from_user['username']

    bot.delete_message(
        chat_id=chat_id, message_id=update.message.message_id
    )
    bot.delete_message(
        chat_id=chat_id,  message_id=settings.QUERY_ID
    )

    print(update.message.text)
    if update.message.text in settings.CLUBS_TG_ID.keys():
        club_db_id = settings.CLUBS_TG_ID[update.message.text]
        t_info = take_club_from_db(club_db_id)
        logo_link = t_info[12]
        bot.send_photo(
            chat_id=chat_id, photo=logo_link,
            caption=settings.my_club_text(t_info),
            reply_markup=InlineKeyboardMarkup(settings.LAST_CHOICE),
            parse_mode="Markdown"
        )
        # добавляем пользователя в базу данных
        bot_user.add_user(tg_fullname, tg_nickname, chat_id, club_db_id)


def add_user_in_db(bot, update):
    # переходной блок, информируем о том что юзер добавлен в базу данных
    query = update.callback_query
    bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f"Я запомнил твой выбор",
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown'
    )


def change_club(bot, update):
    # блок, интересуемся действительно ли пользователь решил сменить клуб?
    query = update.callback_query
    bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f"Решил выбрать другой клуб?",
        reply_markup=InlineKeyboardMarkup(settings.CHANGE_CLUB),
        parse_mode='Markdown'
    )


def main_menu(bot, update):
    # вывод МЕНЮ, либо через прямые сообщения, либо через возврат
    try:
        chat_id = update.message.chat_id
        status = bot_user.check_in_db(chat_id)
        if status:
            try:
                query = update.callback_query
                chat_id = query.message.chat_id
                bot.delete_message(
                    chat_id=chat_id,
                    message_id=query.message.message_id
                )
                bot.send_message(
                    chat_id=chat_id,
                    message_id=query.message.message_id,
                    text=f">>>> *ОСНОВНОЕ МЕНЮ* <<<<",
                    reply_markup=InlineKeyboardMarkup(settings.MAIN_MENU_KEYS),
                    parse_mode='Markdown'
                )
            except AttributeError:
                chat_id = update.message.chat_id
                bot.send_message(
                    chat_id=chat_id,
                    message_id=update.message.message_id,
                    text=f">>>> *ОСНОВНОЕ МЕНЮ* <<<<",
                    reply_markup=InlineKeyboardMarkup(settings.MAIN_MENU_KEYS),
                    parse_mode='Markdown'
                )
        else:
            bot.delete_message(
                chat_id=update.message.chat_id, message_id=update.message.message_id
            )
    except AttributeError:
        try:
            query = update.callback_query
            chat_id = query.message.chat_id
            bot.delete_message(
                chat_id=chat_id,
                message_id=query.message.message_id
            )
            bot.send_message(
                chat_id=chat_id,
                message_id=query.message.message_id,
                text=f">>>> *ОСНОВНОЕ МЕНЮ* <<<<",
                reply_markup=InlineKeyboardMarkup(settings.MAIN_MENU_KEYS),
                parse_mode='Markdown'
            )
        except AttributeError:
            chat_id = update.message.chat_id
            bot.send_message(
                chat_id=chat_id,
                message_id=update.message.message_id,
                text=f">>>> *ОСНОВНОЕ МЕНЮ* <<<<",
                reply_markup=InlineKeyboardMarkup(settings.MAIN_MENU_KEYS),
                parse_mode='Markdown'
            )


def match_links(bot, update):
    # вывод ссылок на трансляции
    query = update.callback_query
    chat_id = query.message.chat_id
    club_db_id = bot_user.take_club_id(chat_id)
    club_page_link = stream_links.take_link(club_db_id)
    game_page_link = stream_links.main(club_page_link)
    all_stream_links = stream_links.get_stream_links(game_page_link)
    club_url = ten_matches.club_link(club_db_id)
    if ten_matches.check_NG_update(club_db_id):
        next_matches = ten_matches.get_next_games_from_db(club_db_id)
    else:
        all_matches = ten_matches.main(club_url)
        ten_matches.load_games_in_db(all_matches, club_db_id, 'NG')
        next_matches = ten_matches.next_games(all_matches)
    if all_stream_links is not False:
        sop_links = stream_links.sopcast_links(all_stream_links)
        ace_links = stream_links.acestream_links(all_stream_links)
        info = ten_matches.get_today_match_from_db(club_db_id)
    else:
        sop_links, ace_links, info = None, None, None

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=query.message.message_id,
        text=settings.match_link_text(sop_links, ace_links, info, next_matches),
        reply_markup=InlineKeyboardMarkup(settings.LINKS),
        parse_mode='Markdown'
    )


def alarm(bot, update):
    # функция настройки уведомлений
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'''Включить уведомление о ближайшей игре?''',
        reply_markup=InlineKeyboardMarkup(settings.ALARM),
        parse_mode='Markdown'
    )


def no_alarm(bot, update):
    # функция отмены уведомлений
    query = update.callback_query
    bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'''Я больше не буду присылать уведомления''',
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown'
    )


def yes_alarm(bot, update):
    # функция подтверждения уведомлений
    query = update.callback_query
    bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=f'''*Уведомление придет тебе за 10 минут до игры*''',
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown'
    )


def next_match(bot, update):
    # вывод инфы о следующем матче
    query = update.callback_query
    chat_id = query.message.chat_id
    club_db_id = bot_user.take_club_id(chat_id)
    club_url = ten_matches.club_link(club_db_id)
    if ten_matches.check_NG_update(club_db_id):
        next_matches = ten_matches.get_next_games_from_db(club_db_id)
    else:
        all_matches = ten_matches.main(club_url)
        ten_matches.load_games_in_db(all_matches, club_db_id, 'NG')
        next_matches = ten_matches.next_games(all_matches)

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=query.message.message_id,
        text=settings.next_or_last_games_text(next_matches, None),
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown'
    )


def last_match(bot, update):
    # вывод инфы о прошедших матчах
    query = update.callback_query
    chat_id = query.message.chat_id
    club_db_id = bot_user.take_club_id(chat_id)
    club_url = ten_matches.club_link(club_db_id)
    if ten_matches.check_LG_update(club_db_id):
        last_matches = ten_matches.get_last_games_from_db(club_db_id)
    else:
        all_matches = ten_matches.main(club_url)
        ten_matches.load_games_in_db(all_matches, club_db_id, 'LG')
        last_matches = ten_matches.last_games(all_matches)

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=query.message.message_id,
        text=settings.next_or_last_games_text(None, last_matches),
        reply_markup=InlineKeyboardMarkup(settings.LAST_GAME),
        parse_mode='Markdown'
    )


def last_match_more(bot, update):
    # подробная информация о прошедших матчах
    query = update.callback_query
    chat_id = query.message.chat_id
    club_db_id = bot_user.take_club_id(chat_id)
    url = stream_links.take_link(club_db_id)

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=query.message.message_id,
        text=settings.more_about_last_matches(url),
        reply_markup=InlineKeyboardMarkup(settings.LAST_GAME_MORE),
        parse_mode='Markdown'
    )


def current_table(bot, update):
    # таблица чемпионата
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=settings.epl_table(),
        reply_markup=InlineKeyboardMarkup(settings.MENU_BUTTON),
        parse_mode='Markdown'
    )


def my_club_info(bot, update):
    # вывод информации о моем клубе, после выбора из МЕНЮ
    query = update.callback_query
    chat_id = query.message.chat_id

    bot.delete_message(
        chat_id=chat_id, message_id=query.message.message_id
    )

    club_db_id = bot_user.take_club_id(chat_id)
    t_info = take_club_from_db(club_db_id)
    logo_link = t_info[12]
    bot.send_photo(
        chat_id=chat_id, photo=logo_link,
        caption=settings.my_club_text(t_info),
        reply_markup=InlineKeyboardMarkup(settings.MY_CLUB_MENU),
        parse_mode="Markdown"
    )


def about_me(bot, update):
    # об авторе
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

    dp.add_handler(MessageHandler(Filters.text, clean))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('restart', start))
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
    dp.add_handler(CallbackQueryHandler(no_alarm, pattern='say_no'))
    dp.add_handler(CallbackQueryHandler(yes_alarm, pattern='say_yes'))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
