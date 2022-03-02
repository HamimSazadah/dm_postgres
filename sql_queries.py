# DROP TABLES

songplay_table_drop = "DROP TABLE if exists songplay;"
user_table_drop = "DROP TABLE if exists  users;"
song_table_drop = "DROP TABLE if exists  songs;"
artist_table_drop = "DROP TABLE if exists  artists;"
time_table_drop = "DROP TABLE if exists  time;"

# CREATE TABLES

songplay_table_create = ("""
create table songplays (songplay_id serial primary key, start_time varchar, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);
""")

user_table_create = ("""
create table users(user_id varchar not null primary key, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""
create table songs(song_id varchar not null primary key, title varchar, artist_id varchar, year int, duration float);
""")

artist_table_create = ("""
create table artists(artist_id varchar not null primary key, name varchar, location varchar, latitude varchar, longitude varchar);
""")

time_table_create = ("""
create table time (start_time varchar not null primary key, hour int, day int, week int, month int, year int, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values (%s,%s,%s,%s,%s,%s,%s,%s) ;
""")

user_table_insert = ("""
insert into users values(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
insert into songs values(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
insert into artists values(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
insert into time values(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT a.song_id,a.artist_id from songs a join artists b on a.artist_id =b.artist_id where title=%s and name=%s and duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]