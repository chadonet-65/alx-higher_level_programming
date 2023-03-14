-- AVG temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY value;
