import sqlite3

db = sqlite3.connect("club_epl_18-19.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE clubs
                (club_id INT PRIMARY KEY, name)
               """)
cursor.execute("""CREATE TABLE unique_info
                (club_id INT REFERENCES clubs(club_id), emblem_link,
                full_club_name, nickname, founded,
                country_id INT REFERENCES country(country_id),
                color_id INT REFERENCES color(color_id),
                stadium_id INT REFERENCES stadium(stadium_id), homepage)
               """)
cursor.execute("""CREATE TABLE country
                (country_id INT PRIMARY KEY, name, emoji_flag_code)
               """)
cursor.execute("""CREATE TABLE color
                (color_id INT PRIMARY KEY, name, emoji_code)
               """)
cursor.execute("""CREATE TABLE stadium
                (stadium_id INT PRIMARY KEY, name, capacity, address)
               """)
