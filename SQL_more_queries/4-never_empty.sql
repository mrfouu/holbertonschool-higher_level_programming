-- This script creates a table named 'id_not_null' if it does not already exist.
-- The table contains two columns:
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
