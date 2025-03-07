-- This script lists all cities with their corresponding state names.
-- Each record displays: cities.id - cities.name - states.name.
-- The results are sorted by cities.id in ascending order.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
