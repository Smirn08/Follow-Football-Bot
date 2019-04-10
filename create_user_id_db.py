import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE users
                (user_id INT , club_id INT)
               """)

cursor.execute("""CREATE UNIQUE INDEX unique_user ON users(user_id)
               """)    

db.commit()
db.close()
