from datetime import datetime
from telegram import InlineKeyboardButton


USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

# KEYBOARDS
MAIN_MENU_KEYS = [
    [
        InlineKeyboardButton('Трансляции', callback_data='links'),
        InlineKeyboardButton('Турнирная таблица', callback_data='table')
    ],
    [
        InlineKeyboardButton('Сыгранные матчи', callback_data='last'),
        InlineKeyboardButton('Будущие Матчи', callback_data='next')
    ],
    [
        InlineKeyboardButton('Мой клуб', callback_data='my_club'),
        InlineKeyboardButton('Об авторе', callback_data='about')
    ]
]

LINKS = [
    [
        InlineKeyboardButton('Уведомления', callback_data='alarm'),
        InlineKeyboardButton('МЕНЮ', callback_data='menu')
    ]
]

ALARM = [
    [
        InlineKeyboardButton('<', callback_data='links'),
        InlineKeyboardButton('Нет', callback_data='say_no'),
        InlineKeyboardButton('Да', callback_data='say_yes')
    ]
]

LAST_GAME = [
    [
        InlineKeyboardButton('Подробнее', callback_data='game'),
        InlineKeyboardButton('МЕНЮ', callback_data='menu')
    ]
]

LAST_GAME_MORE = [
    [
        InlineKeyboardButton('<', callback_data='last'),
        InlineKeyboardButton('МЕНЮ', callback_data='menu')
    ]
]

MY_CLUB_MENU = [
    [
        InlineKeyboardButton('Сменить клуб', callback_data='change'),
        InlineKeyboardButton('МЕНЮ', callback_data='menu')
    ]
]

ABOUT_BUTTONS = [
    [
        InlineKeyboardButton(
            'press F to pay respect',
            url='https://t.me/Smirn08'
        ),
        InlineKeyboardButton('МЕНЮ', callback_data='menu')
    ]
]

MENU_BUTTON = [
    [InlineKeyboardButton('МЕНЮ', callback_data='menu')]
]

START_KEYS = [
    [InlineKeyboardButton('Выбрать клуб', callback_data='p1')]
]

CHANGE_CLUB = [
    [InlineKeyboardButton('Да! Решил выбрать другой!', callback_data='p1')],
    [InlineKeyboardButton('Нет. Передумал...', callback_data='menu')]
]

FIRST_PAGE_KEYS = [
    [InlineKeyboardButton('>', callback_data='p2')]
]

SECOND_PAGE_KEYS = [
    [
        InlineKeyboardButton('|<', callback_data='p1'),
        InlineKeyboardButton('>', callback_data='p3')
    ]
]

THIRD_PAGE_KEYS = [
    [
        InlineKeyboardButton('<', callback_data='p2'),
        InlineKeyboardButton('>|', callback_data='p4')
    ]
]

FORTH_PAGE_KEYS = [
    [InlineKeyboardButton('<', callback_data='p3')]
]

LAST_CHOICE = [
    [InlineKeyboardButton('Подтвердить выбор', callback_data='add_user')],
    [InlineKeyboardButton('Выбрать другой клуб', callback_data='change')]
]

###############################################################################

COLORS = (
    {
        'id': 101,
        'name': 'red black',
        'emoji': '🔴 ⚫️'
        },
    {
        'id': 102,
        'name': 'red white',
        'emoji': '🔴 ⚪️'
        },
    {
        'id': 103,
        'name': 'blue white',
        'emoji': '🔵 ⚪️'
        },
    {
        'id': 104,
        'name': 'red blue',
        'emoji': '🔴 🔵'
        },
    {
        'id': 105,
        'name': 'blue yellow',
        'emoji': '🔵 💛'
        },
    {
        'id': 106,
        'name': 'white red black',
        'emoji': '⚪️ 🔴 ⚫️'
        },
    {
        'id': 107,
        'name': 'red white black',
        'emoji': '🔴 ⚪️ ⚫️'
        },
    {
        'id': 108,
        'name': 'black yellow',
        'emoji': '⚫️ 💛'
        },
    {
        'id': 109,
        'name': 'black white',
        'emoji': '⚫️ ⚪️'
        }
)

COUNTRY = (
    {
        'id': 201,
        'name': 'England',
        'emoji': '🏴󠁧󠁢󠁥󠁮󠁧󠁿'
        },
    {
        'id': 202,
        'name': 'Wales',
        'emoji': '🏴󠁧󠁢󠁷󠁬󠁳󠁿'
        }
)

CLUB_COMMAND_LIST = [
        'bou', 'ars', 'brh', 'bur', 'cdf',
        'che', 'cry', 'eve', 'ful', 'hdd',
        'lei', 'liv', 'mci', 'mun', 'new',
        'sou', 'tot', 'wat', 'whu', 'wlv'
]

CLUBS_TG_ID = {
        '/bou': 1, '/ars': 2, '/brh': 3, '/bur': 4, '/cdf': 5,
        '/che': 6, '/cry': 7, '/eve': 8, '/ful': 9, '/hdd': 10,
        '/lei': 11, '/liv': 12, '/mci': 13, '/mun': 14, '/new': 15,
        '/sou': 16, '/tot': 17, '/wat': 18, '/whu': 19, '/wlv': 20
}

LIST_ONE = f'''*AFC Bournemouth*
/bou
*Arsenal FC*
/ars
*Brighton & Hove Albion*
/brh
*Burnley FC*
/bur
*Cardiff City*
/cdf'''

LIST_TWO = f'''*Chelsea FC*
/che
*Crystal Palace*
/cry
*Everton FC*
/eve
*Fulham FC*
/ful
*Huddersfield Town*
/hdd'''

LIST_THREE = f'''*Leicester City*
/lei
*Liverpool FC*
/liv
*Manchester City*
/mci
*Manchester United*
/mun
*Newcastle United*
/new'''

LIST_FOUR = f'''*Southampton FC*
/sou
*Tottenham Hotspur*
/tot
*Watford FC*
/wat
*West Ham United*
/whu
*Wolverhampton Wanderers*
/wlv'''

ABOUT = f'''bot by [Maksim Smirnov](github.com/Smirn08)'''

QUERY_ID = None

CLUB_ID = None


def my_club_text(t_info):
    # блок текста с информацией о клубе
    text = f'''*{t_info[2]}* {t_info[6]}
{t_info[3]} | {t_info[8]}

*Founded:* {t_info[4]}

*Home:* {t_info[9]}
*Capacity:* {t_info[10]}
*Address:* {t_info[11]}

*Web:* [{t_info[13].replace('http://','')
                    .replace('https://','')}]({t_info[13]})'''
    return text


def next_or_last_games_text(next=None, last=None):
    # блок текста вывода информации о матчах
    text = ''
    if next is None:
        if len(last) == 0:
            text = f'_Ваш клуб не сыграл ни одного матча в этом сезоне_'
        else:
            for item in last[:5]:
                text += f"""\n{item['date']}
{item['home']} *{item['result_or_time']}* {item['away']}\n"""
    if last is None:
        if len(next) == 0:
            text = f'_Ваш клуб сыграл все матчи в этом сезоне_'
        else:
            for item in next:
                text += f"""\n{item['date']}
{item['home']} - {item['away']} | *{item['result_or_time']}* (MSK)\n"""

    return text


def match_link_text(ace=None, sop=None, info=None, next=None):
    # блок текста ссылок на матчи
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')
    if info is not None:
        text = f"{info[0]} | {info[2]} (MSK)\n{info[1]} - {info[3]}\n"
        if sop is not None:
            text += "\n✔️*SopCast:*\n"
            for item in sop:
                text += f"{item['link']} ({item['kbs']})\n"
        if ace is not None:
            text += "\n✔️*Ace Stream:*\n"
            for item in ace:
                text += f"{item['link']} ({item['kbs']})\n"
    for item in next[:1]:
        if item['unique_code'][0:10] == data_str:
            text = f"""Сегодня *{item['date']}* в *{item['result_or_time']} (MSK)* игра!

{item['home']} - {item['away']}\n"""
            text += f'*\nСсылки  появятся за 2 минуты до матча*\n'
        else:
            text = f'*Ваш клуб сегодня не играет*\n'
            text += f"""\nБлижайшая игра:
{item['date']} | *{item['result_or_time']}* (MSK)
{item['home']} - {item['away']}\n"""

    return text


def epl_table():
    # функция вывода текста с таблицей АПЛ
    text = f'''
    [Таблица АПЛ 2018/19](http://www.espn.com/soccer/standings/_/league/eng.1)
    '''
    return text


def more_about_last_matches(url):
    # ссылка на информацию о матчах
    text = f'''
    [НАЖМИ СЮДА ДЛЯ ПРОСМОТРА ИНФОРМАЦИИ]({url})
    '''
    return text
