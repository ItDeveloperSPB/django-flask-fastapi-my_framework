
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS type_course;
DROP TABLE IF EXISTS course;
CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                      name VARCHAR (32));

CREATE TABLE type_course (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                          name VARCHAR (32));

CREATE TABLE course (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                     name VARCHAR (32),
                     type_id INTEGER NOT NULL,
                     FOREIGN KEY (type_id) REFERENCES type_course(id));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
