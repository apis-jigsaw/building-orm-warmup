CREATE TABLE IF NOT EXISTS users (
   id serial PRIMARY KEY,
   name varchar(250),
   birthday varchar(250)
);

CREATE TABLE IF NOT EXISTS venues (
   id serial PRIMARY KEY,
   name varchar(250),
);

