-- AVG temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures AS s GROUP BY s.value;
