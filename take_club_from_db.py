import sqlite3


def take_club_from_db(club_id):

    conn = sqlite3.connect('club_epl_18-19.db')
    cursor = conn.cursor()

    cursor.execute(f'''SELECT clubs.club_id,
                            clubs.name,
                            unique_info.full_club_name,
                            unique_info.nickname,
                            unique_info.founded,
                            country.name,
                            country.emoji_flag_code,
                            color.name,
                            color.emoji_code,
                            stadium.name,
                            stadium.capacity,
                            stadium.address,
                            unique_info.emblem_link,
                            unique_info.homepage
                    FROM clubs
                    INNER JOIN unique_info
                        ON clubs.club_id = unique_info.club_id
                    INNER JOIN country
                        ON unique_info.country_id = country.country_id
                    INNER JOIN color
                        ON unique_info.color_id = color.color_id
                    INNER JOIN stadium
                        ON unique_info.stadium_id = stadium.stadium_id
                    WHERE clubs.club_id = '{club_id}'
                    ''')

    results = cursor.fetchall()

    for info in results:
        t_info = info

    # club_id = t_info[0]
    # club_name = t_info[1]
    # full_club_name = t_info[2]
    # nickname = t_info[3]
    # founded = t_info[4]
    # country_name = t_info[5]
    # country_emoji = emoji.emojize(t_info[6], use_aliases=True)
    # clr_name = t_info[7]
    # clr_emoji = emoji.emojize(t_info[8], use_aliases=True)
    # st_name = t_info[9]
    # st_capacity = t_info[10]
    # st_address = t_info[11]
    # embl_link = t_info[12]
    # site = t_info[13]

    return t_info

