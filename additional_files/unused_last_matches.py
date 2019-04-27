import sqlite3


def take_last_match_from_db(club_id):
    # получить инфу о прошедших матчах с базы данных
    conn = sqlite3.connect('clubs_schedule.db')
    cursor = conn.cursor()

    cursor.execute(f"""SELECT rus_name
                FROM livesport_club_names
                WHERE livesport_club_names.club_id = '{club_id}'
                """)

    name = cursor.fetchone()[0]

    cursor.execute(f"""SELECT date,
                    competition,
                    home_club,
                    result,
                    guest_club
                    FROM last_matches
                    WHERE home_club = '{name}' OR guest_club = '{name}'
                    ORDER BY unique_code DESC
                    """)

    match_info = cursor.fetchall()
    return match_info


def print_result(match_info):
    # блок выводов результата прошедших матчей
    LIST = []
    for elements in match_info:
        LIST.append(elements[0])
        LIST.append(elements[1])
        LIST.append(elements[2])
        LIST.append(elements[3])
        LIST.append(elements[4])
    text = f'''{LIST[0]} | ({LIST[1]})
{LIST[2]} {LIST[3]} {LIST[4]}

{LIST[5]} | ({LIST[6]})
{LIST[7]} {LIST[8]} {LIST[9]}

{LIST[10]} | ({LIST[11]})
{LIST[12]} {LIST[13]} {LIST[14]}

{LIST[15]} | ({LIST[16]})
{LIST[17]} {LIST[18]} {LIST[19]}

{LIST[20]} | ({LIST[21]})
{LIST[22]} {LIST[23]} {LIST[24]}'''

    return text
