import sqlite3


def check_user_in_db(user_tg_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_tg_id}'")
    data = cursor.fetchall()
    if len(data) == 0:
        print(f"There is no users named: '{user_tg_id}'")
        return False
    else:
        cursor.execute(f"SELECT club_id FROM users WHERE users.user_id = '{user_tg_id}'")
        data = cursor.fetchone()[0]
        print(f'Name: {user_tg_id} - club_id: {data}')
        return True


def add_user(user_tg_id, user_club_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"REPLACE INTO users VALUES('{user_tg_id}', {user_club_id})")

    conn.commit()
    conn.close()


def take_club_id(user_tg_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_tg_id}'")
    data = cursor.fetchall()
    for info in data:
        club_id = info[1]

    return club_id