# CIT-223-018/2021 Anderson Macharia Kinyua
# The README contains instructions on how to execute the following code

import psycopg2

connection = psycopg2.connect('dbname = artist')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS artists;')
cursor.execute('DROP TABLE IF EXISTS album;')
cursor.execute('DROP TABLE IF EXISTS track;')
cursor.execute('DROP TABLE IF EXISTS wasplayedat;')

cursor.execute('''CREATE TABLE  artists(artist_id INTEGER PRIMARY KEY,artist_name varchar(255) NOT NULL UNIQUE);''')

cursor.execute('CREATE TABLE album(album_id INTEGER PRIMARY KEY, album_name varchar(200) NOT NULL,artist_id INTEGER);')

cursor.execute('''CREATE TABLE track(track_id INTEGER PRIMARY KEY, track_name varchar(100) UNIQUE,
        track_time INTEGER, album_id INTEGER, wasplayedat_id INTEGER);''')

cursor.execute('CREATE TABLE wasplayedat(wasplayedat_id INTEGER PRIMARY KEY, played varchar(200), track_id INTEGER);')

cursor.execute('''INSERT INTO artists(artist_id, artist_name) VALUES(1, 'Drake');''')
cursor.execute('''INSERT INTO artists(artist_id, artist_name) VALUES(2, 'Becky G');''')

cursor.execute('''INSERT INTO album(album_id, album_name, artist_id) VALUES(1, 'NON STOP', 1);''')
cursor.execute('''INSERT INTO album(album_id, album_name, artist_id) VALUES(2, 'Cant stop dancin', 2);''')

cursor.execute('''INSERT INTO track(track_id, track_name, track_time, album_id, wasplayedat_id) VALUES(1,'Savage',12, 1, 3);''')
cursor.execute('''INSERT INTO track(track_id, track_name, track_time, album_id, wasplayedat_id) VALUES(2,'Fantastic',5, 2, 4);''')


cursor.execute('''INSERT INTO wasplayedat(wasplayedat_id, played, track_id) VALUES(3, 'Kanairo', 1);''')
cursor.execute('''INSERT INTO wasplayedat(wasplayedat_id, played, track_id) VALUES(4, 'Horn Bill', 2);''')

cursor.execute('SELECT * FROM artists;')
result = cursor.fetchall()
print(result)

cursor.execute('SELECT * FROM album;')
result = cursor.fetchone()
print(result)

cursor.execute('SELECT * FROM track;')
result = cursor.fetchmany()
print(result)

cursor.execute('SELECT * FROM wasplayedat;')
result = cursor.fetchall()
print(result)

connection.commit()

connection.close()
cursor.close()


