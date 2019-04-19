from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import datetime
import locale


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_last_mathes(html):
    # парсинг web страницы, чтоб получить результаты последних 5 игр
    LAST_RESULTS = []
    soup = BeautifulSoup(html, 'html.parser')
    soup_date = soup.find_all('span', class_='date')[1:]
    competition = soup.find_all('span', class_='competition')
    clubs = soup.find_all('div', class_='commands')

    for i in range(0, len(soup_date)):
        date = soup_date[i].text
        clear_date = date.replace('ря', 'рь').replace('ля', 'ль').replace(
            'та', 'т').replace('ая', 'ай').replace('ня', 'нь')
        comp = competition[i].text
        match_result_text = clubs[i].text.split()
        home_club = None
        score = None
        guest_club = None
        if len(match_result_text) >= 6 and len(match_result_text[1]) > 2:
            home_club = ' '.join(match_result_text[:2])
            score = ' '.join(match_result_text[2:5])
            guest_club = ' '.join(match_result_text[5:])
        elif len(match_result_text) == 6 and len(match_result_text[1]) < 2:
            home_club = ''.join(match_result_text[:1])
            score = ' '.join(match_result_text[1:4])
            guest_club = ' '.join(match_result_text[4:])
        else:
            home_club = ''.join(match_result_text[0])
            score = ' '.join(match_result_text[1:4])
            guest_club = ''.join(match_result_text[4])
        locale.setlocale(locale.LC_ALL, 'russian')
        take_data = datetime.strptime(clear_date, '%d %B %Y')
        data_str = take_data.strftime('%Y-%m-%d')
        unique_code = f'{data_str}-{home_club[0:3].upper()}-{guest_club[0:3].upper()}'
        LAST_RESULTS.append({
            'date': date,
            'result': score,
            'competition': comp,
            'home': home_club,
            'away': guest_club,
            'unique_str_code': unique_code
        })

    load_last_matches_in_db(LAST_RESULTS)


def load_last_matches_in_db(LAST_RESULTS):
    # загрузка полученных данных в web в базу данных
    db = sqlite3.connect("clubs_schedule.db")
    cursor = db.cursor()

    for games in LAST_RESULTS:
        cursor.execute(f'''REPLACE INTO last_matches (date, competition, result,
                home_club, guest_club, unique_code)
                VALUES (:date, :competition, :result,
                :home, :away, :unique_str_code)''', games)

    db.commit()
    db.close()


def main(link):
    html = get_html(link)
    if html:
        get_last_mathes(html)


def take_link(club_id):
    # получение ссылки из базы данных, которую надо парсить
    conn = sqlite3.connect('clubs_schedule.db')
    cursor = conn.cursor()

    cursor.execute(f"""SELECT link
                FROM livesport_club_names
                WHERE livesport_club_names.club_id = '{club_id}'
                """)

    link = cursor.fetchone()[0]

    main(link)
