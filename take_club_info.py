from bs4 import BeautifulSoup
import requests


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_club_info_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_club_links = soup.find('table', class_='standard_tabelle').find_all('td', class_='hell')
    # print(all_club_links)
    # result_links = []
    for lines in all_club_links:
        url = lines.find_all('a')[2]['href']
        print(url)
#         result_links.append({
#                     'url': url,
#                     })
# print(result_links)    


if __name__ == "__main__":
    html = get_html("https://www.worldfootball.net/players/eng-premier-league-2018-2019/")
    if html:
        get_club_info_links(html)
