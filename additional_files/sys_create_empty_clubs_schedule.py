import sqlite3

db = sqlite3.connect("clubs_schedule.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE livesport_club_names
                (club_id INT, eng_name,
                rus_name, short_name, link)
                """)
cursor.execute("""CREATE TABLE upcoming_matches
                (date, time, home_club, guest_club)
                """)
cursor.execute("""CREATE TABLE last_matches
                (date, competition, result, home_club, guest_club, unique_code)
                """)

cursor.execute("""CREATE UNIQUE INDEX unique_code ON last_matches(unique_code)
               """)

db.commit()
db.close()
