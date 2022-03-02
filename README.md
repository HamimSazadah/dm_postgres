## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
Sparkify need an easy way to query their data, so they can analyze their data quick and easy.
## How to run the Python scripts
1. run script for reset the database 
`python create_tables.py`
2. run etl.py for doing etl to database
`python etl.py`
## An explanation of the files in the repository
- files in data/song_data, include many data about songs in json format. ex:
`{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}`
- files in data/log_data, include many data about logs song played in music streaming apps in json format. ex:
`{"artist":"N.E.R.D. FEATURING MALICE","auth":"Logged In","firstName":"Jayden","gender":"M","itemInSession":0,"lastName":"Fox","length":288.9922,"level":"free","location":"New Orleans-Metairie, LA","method":"PUT","page":"NextSong","registration":1541033612796.0,"sessionId":184,"song":"Am I High (Feat. Malice)","status":200,"ts":1541121934796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.3; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"101"}`
## State and justify your database schema design and ETL pipeline.
### database schema: 
- songplays (songplay_id serial primary key, start_time varchar, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);
- users(user_id varchar not null primary key, first_name varchar, last_name varchar, gender varchar, level varchar);
- songs(song_id varchar not null primary key, title varchar, artist_id varchar, year int, duration float);
- artists(artist_id varchar not null primary key, name varchar, location varchar, latitude varchar, longitude varchar);
- time (start_time varchar not null primary key, hour int, day int, week int, month int, year int, weekday int);
### ETL:
json file > postgres db