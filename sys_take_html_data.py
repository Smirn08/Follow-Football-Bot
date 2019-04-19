import requests
# формирование html страницы epl 18-19


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


if __name__ == "__main__":
    html = get_html("https://www.worldfootball.net/players/eng-premier-league-2018-2019/")
    if html:
        with open("wf_epl_2018-2019.html", "w", encoding="utf8") as f:
            f.write(html)
