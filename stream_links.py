import sqlite3
import requests
from bs4 import BeautifulSoup


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
        return get_main_game_link(html)


def take_link(club_id):
    # получение ссылки из базы данных, которую надо парсить
    conn = sqlite3.connect('clubs_schedule.db')
    cursor = conn.cursor()

    cursor.execute(f"""SELECT link
                FROM livesport_club_names
                WHERE livesport_club_names.club_id = '{club_id}'
                """)

    link = cursor.fetchone()[0]
    return link


def get_main_game_link(html):
    # парсинг web страницы, чтоб получить страницу игры
    soup = BeautifulSoup(html, 'html.parser')
    main_link = soup.find_all('a', class_='dark-btn')
    for element in main_link:
        main_link = 'https://livesport.ws' + element['href']
    return main_link


def get_stream_links(main_link):
    # парсинг ссылок на трансляции
    ALL_LINKS = []
    try:
        result = requests.get(main_link)
        html = result.text
        soup = BeautifulSoup(html, 'html.parser')
        head_name = soup.find_all('ul', class_='broadcasting-types')
        for games in head_name:
            html_links = games.find_all('a', class_='dark-btn')
            lk = []
            for links in html_links:
                links = links['href']
                lk.append(links)
            lk.reverse()

            html_speed = games.find_all('td', class_='speed')
            kbs = []
            for speed in html_speed:
                speed = speed.text
                kbs.append(speed)

            lim = len(kbs)
            lk = lk[:lim]
            lk = lk[::-1]

            keys = ['link', 'kbs']
            zipped = zip(lk, kbs)

            ALL_LINKS = [dict(zip(keys, values)) for values in zipped]

        if len(ALL_LINKS) > 0:
            return ALL_LINKS
        else:
            return False
    except requests.exceptions.MissingSchema:
        return False


def sopcast_links(ALL_LINKS):
    # ссылки на sopcast
    sopcast = []
    for links in ALL_LINKS:
        if links['link'][0:3] == 'sop':
            sopcast.append(links)
    return sopcast


def acestream_links(ALL_LINKS):
    # ссылки на acestream
    acestream = []
    for links in ALL_LINKS:
        if links['link'][0:3] == 'ace':
            acestream.append(links)
    return acestream
