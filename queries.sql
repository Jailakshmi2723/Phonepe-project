SELECT year, SUM(amount) FROM aggregated_insurance GROUP BY year;
SELECT quarter, SUM(amount) FROM aggregated_insurance GROUP BY quarter;
SELECT SUM(count) FROM aggregated_insurance;
SELECT AVG(amount) FROM aggregated_insurance;