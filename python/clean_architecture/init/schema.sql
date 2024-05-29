CREATE DATABASE IF NOT EXISTS clean_database;

CREATE SCHEMA IF NOT EXISTS clean_database;

CREATE TABLE IF NOT EXISTS clean_database.users (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age BIGINT NOT NULL
);
