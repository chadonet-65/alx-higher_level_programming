-- List all cities of california
SELECT cities.id, cities.name FROM cities, state  WHERE state.id = cities.state_id AND cities.name = 'California' ORDER BY cities.id ASC;
