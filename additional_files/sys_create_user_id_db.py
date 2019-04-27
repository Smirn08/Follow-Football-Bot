import sqlite3
# создание базы данных пользователей
db = sqlite3.connect("users.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE users
                (tg_full_name, tg_username, tg_user_id INT , club_id INT)
               """)

cursor.execute("""CREATE UNIQUE INDEX unique_user ON users(tg_user_id)
               """)

db.commit()
db.close()
