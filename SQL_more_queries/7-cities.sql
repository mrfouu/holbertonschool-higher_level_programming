-- This script creates the database 'hbtn_0d_usa' and the table 'cities' inside it if they do not already exist.
-- The 'cities' table contains:
-- Create the database if it does not exis
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id
);
