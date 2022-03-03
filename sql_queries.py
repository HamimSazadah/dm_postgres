# DROP TABLES

songplay_table_drop = "DROP TABLE if exists songplay;"
user_table_drop = "DROP TABLE if exists  users;"
song_table_drop = "DROP TABLE if exists  songs;"
artist_table_drop = "DROP TABLE if exists  artists;"
time_table_drop = "DROP TABLE if exists  time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays
  (
     songplay_id SERIAL PRIMARY KEY,
     start_time  VARCHAR NOT NULL,
     user_id     INT NOT NULL,
     level       VARCHAR NOT NULL,
     song_id     VARCHAR,
     artist_id   VARCHAR ,
     session_id  VARCHAR,
     location    VARCHAR,
     user_agent  VARCHAR
  ); 
""")

user_table_create = ("""
CREATE TABLE users
  (
     user_id    int NOT NULL PRIMARY KEY,
     first_name VARCHAR NOT NULL,
     last_name  VARCHAR NOT NULL,
     gender     VARCHAR NOT NULL,
     level      VARCHAR NOT NULL 
  ); 
""")

song_table_create = ("""
CREATE TABLE songs
  (
     song_id   VARCHAR NOT NULL PRIMARY KEY,
     title     VARCHAR NOT NULL,
     artist_id VARCHAR NOT NULL,
     year      INT NOT NULL,
     duration  FLOAT NOT NULL
  ); 
""")

artist_table_create = ("""
CREATE TABLE artists
  (
     artist_id VARCHAR NOT NULL PRIMARY KEY,
     name      VARCHAR NOT NULL,
     location  VARCHAR,
     latitude  FLOAT,
     longitude FLOAT
  ); 
""")

time_table_create = ("""
CREATE TABLE time
  (
     start_time VARCHAR NOT NULL PRIMARY KEY,
     hour       INT NOT NULL,
     day        INT NOT NULL,
     week       INT NOT NULL,
     month      INT NOT NULL,
     year       INT NOT NULL,
     weekday    INT NOT NULL
  ); 
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
            (start_time,
             user_id,
             level,
             song_id,
             artist_id,
             session_id,
             location,
             user_agent)
VALUES      (%s,
             %s,
             %s,
             %s,
             %s,
             %s,
             %s,
             %s); 
""")

user_table_insert = ("""
INSERT INTO users VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        user_id
            )
            DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        song_id
            )
            do nothing;
""")

artist_table_insert = ("""
INSERT INTO artists VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        artist_id
            )
            do UPDATE
set    location = excluded.location,
       latitude = excluded.latitude,
       longitude = excluded.longitude
""")

time_table_insert = ("""
INSERT INTO time VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        start_time
            )
            do nothing;
""")

# FIND SONGS

song_select = ("""
SELECT a.song_id,
       a.artist_id
FROM   songs a
       join artists b
         ON a.artist_id = b.artist_id
WHERE  title = %s
       AND name = %s
       AND duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]