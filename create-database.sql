CREATE DATABASE thoughtcollector;

CREATE USER thought_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE thoughtcollector TO thought_admin;