-- This script creates the database 'hbtn_0d_usa' and the table 'states' inside it if they do not already exist.
-- The 'states' table contains:
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
