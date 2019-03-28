from bs4 import BeautifulSoup
import requests
import json


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
    for club_urls in result_links:
        club_info_url = club_urls['url']
        club_info_html = get_club_info_html(club_info_url)
        soup = BeautifulSoup(club_info_html, 'html.parser')
        all_club_info = soup.find('table', class_='standard_tabelle')
        line_hell = all_club_info.find_all('td', class_='hell')
        line_dunkel = all_club_info.find_all('td', class_='dunkel')
        embl = soup.find('div', class_='emblem')
        embl_link = embl.find('img')
        EPL_CLUBS.append({
            'team': line_hell[1].text,
            'emblem_link': embl_link['src'],
            'full_name': line_hell[3].text,
            'country': line_hell[5].text.replace('\t', '').replace('\n', '').replace('\r', ''),
            'nickname': line_hell[7].text,
            'founded': line_dunkel[1].text,
            'colors': line_dunkel[3].text,
            'stadium': line_hell[9].text.replace('\t', '').replace('\n', ' '),
            'st_capacity': '',
            'st_address': line_hell[11].text.replace('\t', '').replace('\n', '').replace('\r', ''),
            'homepage': line_dunkel[5].text
        })

    print(json.dumps(EPL_CLUBS, indent=4))


if __name__ == "__main__":
    main_url = "https://www.worldfootball.net/players/eng-premier-league-2018-2019/"
    main_html = get_main_html(main_url)
    if main_html:
        get_club_info_links(main_html)
