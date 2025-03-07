-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
-- Créer la base de données hbtn_0d_2 si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
