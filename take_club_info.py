from bs4 import BeautifulSoup
from settings import COLORS
from settings import COUNTRY
import requests
import json
import csv
import sqlite3


def get_main_html(main_url):
    try:
        result = requests.get(main_url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_club_info_links(main_html):
    soup = BeautifulSoup(main_html, 'html.parser')
    all_club_links = soup.find('table', class_='standard_tabelle')
    result_links = []
    dirty_url = all_club_links.find_all("a", string="Info")
    for element in dirty_url:
        clear_url = element.get('href')
        result_links.append({
            'url': 'https://www.worldfootball.net' + clear_url
        })

    get_club_full_info(result_links)


def get_club_info_html(result_links):
    try:
        result = requests.get(result_links)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


# test_url = 'https://www.worldfootball.net/teams/wolverhampton-wanderers/1/'


def get_club_full_info(result_links):
    EPL_CLUBS = []
    id = 0
    for club_urls in result_links:
        id += 1
        club_info_url = club_urls['url']
        club_info_html = get_club_info_html(club_info_url)
        soup = BeautifulSoup(club_info_html, 'html.parser')
        all_club_info = soup.find('table', class_='standard_tabelle')
        line_hell = all_club_info.find_all('td', class_='hell')
        line_dunkel = all_club_info.find_all('td', class_='dunkel')
        embl = soup.find('div', class_='emblem')
        embl_link = embl.find('img')
        st = line_hell[9].text.replace('\t', '').replace('\n', ' ').replace('Ranks', '')
        EPL_CLUBS.append({
            'id': id,
            'name': line_hell[1].text,
            'emblem_link': embl_link['src'],
            'full_name': line_hell[3].text,
            'country':
                line_hell[5].text.replace('\t', '')
                .replace('\n', '')
                .replace('\r', ''),
            'nickname': line_hell[7].text,
            'founded': line_dunkel[1].text,
            'colors': line_dunkel[3].text.replace('-', ' '),
            'stadium':
                ' '.join(st.split(' ')[1:-2])
                .replace('\u00e2', '')
                .replace('\u0080', '')
                .replace('\u0099s', ''),
            'st_capacity': st.split(' ')[-2],
            'st_address':
                line_hell[11].text.replace('\t', '')
                .replace('\n', '')
                .replace('\r', ''),
            'homepage': line_dunkel[5].text
        })

    # print(json.dumps(EPL_CLUBS, indent=4))
    put_epl_clubs_in_db(EPL_CLUBS)

    # with open('EPL_CLUBS.csv', 'w', newline='') as f:
    #     writer = csv.DictWriter(f, fieldnames=EPL_CLUBS[0])
    #     writer.writeheader()
    #     writer.writerows(EPL_CLUBS)


def put_epl_clubs_in_db(EPL_CLUBS):

    db = sqlite3.connect("club_epl_18-19.db")
    cursor = db.cursor()

    for colors in COLORS:
        cursor.execute('''INSERT INTO color (color_id, name, emoji_code)
                    VALUES (:id, :name, :emoji)''', colors)

    for country in COUNTRY:
        cursor.execute('''INSERT INTO country (country_id, name, emoji_flag_code)
                        VALUES (:id, :name, :emoji)''', country)

    st_id = 300
    for stadium in EPL_CLUBS:
        st_id += 1
        cursor.execute(f'''INSERT INTO stadium (stadium_id, name, capacity, address)
                VALUES ({st_id}, :stadium, :st_capacity,
                :st_address)''', stadium)

    for clubs in EPL_CLUBS:

        cursor.execute('''INSERT INTO clubs (club_id, name)
                        VALUES (:id, :name)''', clubs)
        cursor.execute('''INSERT INTO unique_info (club_id, emblem_link,
                        full_club_name, nickname, founded,
                        country_id, color_id, stadium_id, homepage)
                        VALUES (:id, :emblem_link, :full_name, :nickname,
                        :founded, "", "", "", :homepage)''', clubs)

    db.commit()
    db.close()


if __name__ == "__main__":
    main_url = "https://www.worldfootball.net/players/eng-premier-league-2018-2019/"
    main_html = get_main_html(main_url)
    if main_html:
        get_club_info_links(main_html)
