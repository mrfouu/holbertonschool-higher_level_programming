-- This script lists all cities of California from the 'cities' table in the 'hbtn_0d_usa' database.
-- The results are sorted by cities.id in ascending order.
-- California's state_id is fetched by a subquery from the 'states' table.

SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
