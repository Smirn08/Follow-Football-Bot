# парсинг 5 прошедших и 5 будущих матчей со Sportbox
import locale
import sqlite3
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_all_games(html):
    # парсинг web страницы, чтоб получить 10 матчей
    soup = BeautifulSoup(html, 'html.parser')
    all_table = soup.find_all('div', class_='_Sportbox_Spb2015_Components_TableGames_TableGames')
    for games in all_table:
        date = games.find_all('div', class_='games-date-group')
        name = games.find_all('div', class_='name')
        score = games.find_all('span', class_='score')
        time = games.find_all('span', class_='time')

        d = []
        for date in date:
            d.append(date.text + ' 2019')
        d.reverse()
        cd = []
        for date in d:
            clear_date = date.replace('ря', 'рь').replace('ля', 'ль').replace(
                        'та', 'т').replace('ая', 'ай').replace('ня', 'нь')
            locale.setlocale(locale.LC_ALL, 'russian')
            take_data = datetime.strptime(clear_date, '%d %B %Y')
            data_str = take_data.strftime('%Y-%m-%d')
            cd.append(data_str)

        n = []
        for name in name:
            n.append(name.text)
        n.reverse()
        away = n[0::2]
        home = n[1::2]

        s1 = []
        for score in score:
            s1.append(score.text)
        s1.reverse()
        s2 = [no_score for no_score in s1 if no_score not in ['-:-']]
        no_score_count = len(s1) - len(s2)

        t = []
        for time in time:
            t.append(time.text)
        t.reverse()

        tt = []
        for true_time in t:
            hours_min = ':'.join(true_time[i:i+2] for i in range(
                0, len(true_time), 2
            ))
            tt.append(hours_min)
        str = '-:-'
        while no_score_count > 0:
            no_score_count -= 1
            tt.append(str)

        score_and_time = s2 + tt

        uq = []
        for game_date, home_club, away_club in zip(cd, home, away):
            unique_code = f'{game_date}-{home_club[:3].upper()}-{away_club[:3].upper()}'
            uq.append(unique_code)

        keys = ['date', 'home', 'result_or_time', 'away', 'unique_code']
        zipped = zip(d, home, score_and_time, away, uq)

        ALL_GAMES = [dict(zip(keys, values)) for values in zipped]

    return ALL_GAMES


def last_games(ALL_GAMES):
    # прошедшие матчи
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')
    LAST_GAMES = []
    for games in ALL_GAMES:
        if games['unique_code'][0:10] < data_str:
            LAST_GAMES.append(games)

    return LAST_GAMES


def next_games(ALL_GAMES):
    # будущие матчи
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')
    NEXT_GAMES = []
    for games in ALL_GAMES:
        if games['unique_code'][0:10] > data_str:
            NEXT_GAMES.append(games)

    return NEXT_GAMES


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def main(link):
    html = get_html(link)
    if html:
        return get_all_games(html)


def load_games_in_db(ALL_GAMES, club_id, game_type):
    # загрузка полученных данных в базу данных
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')

    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    for games in ALL_GAMES:
        if games['unique_code'][0:10] < data_str and game_type == 'LG':
            cursor.execute(f'''INSERT OR REPLACE INTO last_matches (date, home_club,
                                    result, guest_club, unique_code)
                                VALUES (:date, :home, :result_or_time,
                                    :away, :unique_code)''', games)

            cursor.execute(f'''UPDATE sportbox
                                SET LG_update_time = "{data_str}"
                                WHERE club_id = "{club_id}"
                            ''')

        if games['unique_code'][0:10] > data_str and game_type == 'NG':
            cursor.execute(f'''INSERT OR REPLACE INTO upcoming_matches (date, home_club,
                                    time, guest_club, unique_code)
                                VALUES (:date, :home, :result_or_time,
                                    :away, :unique_code)''', games)

            cursor.execute(f'''UPDATE sportbox
                                SET NG_update_time = "{data_str}"
                                WHERE club_id = "{club_id}"
                            ''')

    print(f'DB {game_type} for club:{club_id} updated today:{data_str}')

    db.commit()
    db.close()


def check_LG_update(club_id):
    # проверка актуальности последних игр в БД
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')

    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    cursor.execute(f'''SELECT LG_update_time
                        FROM sportbox
                        WHERE club_id = "{club_id}"''')
    data = cursor.fetchone()
    for data in data:
        if data == data_str:
            print(f"DB IS UP TO DATE!")
            return True
        else:
            print(f"OLD DB! NEED TO UPDATE.")
            return False


def check_NG_update(club_id):
    # проверка актуальности будущих игр в БД
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')

    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    cursor.execute(f"""SELECT NG_update_time
                        FROM sportbox
                        WHERE club_id = '{club_id}'""")

    data = cursor.fetchone()

    for data in data:
        if data == data_str:
            print(f"DB IS UP TO DATE!")
            return True
        else:
            print(f"OLD DB! NEED TO UPDATE.")
            return False


def get_last_games_from_db(club_id):
    # получение прошедших матчей с БД
    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    cursor.execute(f"""SELECT club_rus_name
                        FROM sportbox
                        WHERE sportbox.club_id = '{club_id}'
                    """)

    name = cursor.fetchone()[0]

    cursor.execute(f"""SELECT date,
                    home_club,
                    result,
                    guest_club,
                    unique_code
                    FROM last_matches
                    WHERE home_club = '{name}' OR guest_club = '{name}'
                    ORDER BY unique_code DESC
                    """)
    data = cursor.fetchall()
    i = -1
    LAST_GAMES = []
    for games in range(0, len(data)):
        i += 1
        LAST_GAMES.append({
            'date': data[i][0],
            'home': data[i][1],
            'result_or_time': data[i][2],
            'away': data[i][3],
            'unique_code': data[i][4]
        })
    return LAST_GAMES


def get_next_games_from_db(club_id):
    # получение будущих матчей с БД
    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    cursor.execute(f"""SELECT club_rus_name
                        FROM sportbox
                        WHERE sportbox.club_id = '{club_id}'
                    """)

    name = cursor.fetchone()[0]

    cursor.execute(f"""SELECT date,
                    home_club,
                    time,
                    guest_club,
                    unique_code
                    FROM upcoming_matches
                    WHERE home_club = '{name}' OR guest_club = '{name}'
                    ORDER BY unique_code ASC
                    """)
    data = cursor.fetchall()

    i = -1
    NEXT_GAMES = []
    for games in range(0, len(data)):
        i += 1
        NEXT_GAMES.append({
            'date': data[i][0],
            'home': data[i][1],
            'result_or_time': data[i][2],
            'away': data[i][3],
            'unique_code': data[i][4]
        })
    return NEXT_GAMES


def get_today_match_from_db(club_id):
    # получение сегодняшнего матча с БД
    today = datetime.today()
    data_str = today.strftime('%Y-%m-%d')

    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    cursor.execute(f"""SELECT club_rus_name
                        FROM sportbox
                        WHERE sportbox.club_id = '{club_id}'
                    """)

    name = cursor.fetchone()[0]

    cursor.execute(f"""SELECT date,
                    home_club,
                    time,
                    guest_club,
                    unique_code
                    FROM upcoming_matches
                    WHERE home_club = '{name}' OR guest_club = '{name}'
                    ORDER BY unique_code ASC
                    """)
    data = cursor.fetchone()

    if data[4][:10] == data_str:
        return data


def club_link(club_id):
    # получение ссылки из базы данных, которую надо парсить
    conn = sqlite3.connect('clubs_schedule.db')
    cursor = conn.cursor()

    cursor.execute(f"""SELECT link
                FROM sportbox
                WHERE sportbox.club_id = '{club_id}'
                """)

    link = cursor.fetchone()[0]

    return link
