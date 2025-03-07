-- This script lists all cities with their corresponding state names.
-- Each record displays: cities.id - cities.name - states.name.
-- The results are sorted by cities.id in ascending order.

SELECT cities.id, cities.name, 
       (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
