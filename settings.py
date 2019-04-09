from telegram import InlineKeyboardButton, InlineKeyboardMarkup

USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

################################ KEYBOARDS ####################################
MAIN_MENU_KEYS = [[InlineKeyboardButton('Трансляции', callback_data='links'),
                    InlineKeyboardButton('Следующий Матч', callback_data='next')],
                [InlineKeyboardButton('Информация о последнем матче', callback_data='last')],
                [InlineKeyboardButton('Турнирная таблица', callback_data='table')],
                [InlineKeyboardButton('Мой клуб', callback_data='my_club'),
                    InlineKeyboardButton('Об авторе', callback_data='about')]]

LINKS = [[InlineKeyboardButton('Уведомления', callback_data='alarm'),
            InlineKeyboardButton('МЕНЮ', callback_data='menu')]]

ALARM = [[InlineKeyboardButton('<', callback_data='links'),
            InlineKeyboardButton('МЕНЮ', callback_data='menu')]]

LAST_GAME = [[InlineKeyboardButton('Подробнее', callback_data='game'),
                InlineKeyboardButton('МЕНЮ', callback_data='menu')]]

MY_CLUB_MENU = [[InlineKeyboardButton('Сменить клуб', callback_data='change'),
                    InlineKeyboardButton('МЕНЮ', callback_data='menu')]]

ABOUT_BUTTONS = [[InlineKeyboardButton('press F to pay respect', url='https://t.me/Smirn08'),
                    InlineKeyboardButton('МЕНЮ', callback_data='menu')]]

MENU_BUTTON = [[InlineKeyboardButton('МЕНЮ', callback_data='menu')]]

START_KEYS = [[InlineKeyboardButton('Выбрать клуб', callback_data='p1')]]

CHANGE_CLUB = [[InlineKeyboardButton('Да! Решил выбрать другой!', callback_data='p1')],
                [InlineKeyboardButton('Нет. Передумал...', callback_data='menu')]]

FIRST_PAGE_KEYS = [[InlineKeyboardButton('>', callback_data='p2')]]

SECOND_PAGE_KEYS = [[InlineKeyboardButton('|<', callback_data='p1'),
                    InlineKeyboardButton('>', callback_data='p3')]]

THIRD_PAGE_KEYS = [[InlineKeyboardButton('<', callback_data='p2'),
                    InlineKeyboardButton('>|', callback_data='p4')]]

FORTH_PAGE_KEYS = [[InlineKeyboardButton('<', callback_data='p3')]]

LAST_CHOICE = [[InlineKeyboardButton('Подтвердить выбор', callback_data='add_user')],
                [InlineKeyboardButton('Выбрать другой клуб', callback_data='change')]]

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
        'afcb', 'afc', 'bha', 'bfc', 'car',
        'cfc', 'cpfc', 'efc', 'ffc', 'htfc',
        'lei', 'lfc', 'mcfc', 'mufc', 'new',
        'sou', 'tot', 'wfc', 'whu', 'wol'
]

CLUBS_TG_ID = {
        '/afcb': 1, '/afc': 2, '/bha': 3, '/bfc': 4, '/car': 5,
        '/cfc': 6, '/cpfc': 7, '/efc': 8, '/ffc': 9, '/htfc': 10,
        '/lei': 11, '/lfc': 12, '/mcfc': 13, '/mufc': 14, '/new': 15,
        '/sou': 16, '/tot': 17, '/wfc': 18, '/whu': 19, '/wol': 20
}

LIST_ONE = f'''*AFC Bournemouth*
/afcb
*Arsenal FC*
/afc
*Brighton & Hove Albion*
/bha
*Burnley FC*
/bfc
*Cardiff City*
/car'''

LIST_TWO = f'''*Chelsea FC*
/cfc
*Crystal Palace*
/cpfc
*Everton FC*
/efc
*Fulham FC*
/ffc
*Huddersfield Town*
/htfc'''

LIST_THREE = f'''*Leicester City*
/lei
*Liverpool FC*
/lfc
*Manchester City*
/mcfc
*Manchester United*
/mufc
*Newcastle United*
/new'''

LIST_FOUR = f'''*Southampton FC*
/sou
*Tottenham Hotspur*
/tot
*Watford FC*
/wfc
*West Ham United*
/whu
*Wolverhampton Wanderers*
/wol'''

ABOUT = f'''bot by [Maksim Smirnov](github.com/Smirn08)'''


# CLUB_PRINT_TEXT = f'''*{t_info[2]}* {t_info[6]}
# {t_info[3]} | {t_info[8]}

# *Founded:* {t_info[4]}

# *Home:* {t_info[9]}
# *Capacity:* {t_info[10]}
# *Address:* {t_info[11]}

# *Web:* [{t_info[13].replace('http://','')
#                    .replace('https://','')}]({t_info[13]})'''
