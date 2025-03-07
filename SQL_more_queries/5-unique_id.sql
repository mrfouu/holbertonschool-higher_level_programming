-- This script creates a table named 'unique_id' if it does not already exist.
-- The table contains two columns:

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
