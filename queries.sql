SELECT year, SUM(amount) FROM aggregated_insurance GROUP BY year;
SELECT quarter, SUM(amount) FROM aggregated_insurance GROUP BY quarter;
SELECT SUM(count) FROM aggregated_insurance;
SELECT AVG(amount) FROM aggregated_insurance;
#mapdata
SELECT state, SUM(amount) AS total_amount
FROM map_insurance
GROUP BY state
ORDER BY total_amount DESC;

--District-wise transaction analysis
SELECT district, SUM(amount) AS total_amount
FROM map_insurance
GROUP BY district
ORDER BY total_amount DESC;
#topdata
SELECT state, SUM(amount) AS total_amount
FROM top_insurance
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;
#yearwise
SELECT year, state, SUM(amount) AS total_amount
FROM top_insurance
GROUP BY year, state
ORDER BY year, total_amount DESC;
#averageperformancebystate
SELECT state, AVG(amount) AS avg_amount
FROM top_insurance
GROUP BY state
ORDER BY avg_amount DESC;