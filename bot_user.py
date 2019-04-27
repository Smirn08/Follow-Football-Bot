import sqlite3


def check_in_db(user_tg_id):
    # проверка юзера по базе
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE tg_user_id = '{user_tg_id}'")
    data = cursor.fetchall()
    if len(data) == 0:
        print(f"NEW USER: '{user_tg_id}'")
        return False
    else:
        cursor.execute(f"SELECT club_id FROM users WHERE users.tg_user_id = '{user_tg_id}'")
        data = cursor.fetchone()[0]
        print(f'USER SELECTED: id: {user_tg_id} - club_id: {data}')
        return True


def add_user(tg_fullname, tg_nickname, user_tg_id, user_club_id):
    # добавление нового юзера в базу
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR REPLACE INTO users VALUES('{tg_fullname}', '{tg_nickname}', '{user_tg_id}', {user_club_id})")
    print(f'NEW USER ADDED or UPDATED: id: {user_tg_id} - club_id: {user_club_id}')

    conn.commit()
    conn.close()


def take_club_id(user_tg_id):
    # получить club id юзера
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE tg_user_id = '{user_tg_id}'")
    data = cursor.fetchall()
    for info in data:
        club_id = info[3]

    return club_id
