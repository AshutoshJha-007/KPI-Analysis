-- KPI Queries

SELECT SUM(revenue) AS total_revenue FROM data;

SELECT AVG(sessions) AS avg_sessions FROM data;

SELECT SUM(users)/SUM(sessions) AS conversion_rate FROM data;

-- Growth Analysis
SELECT date,
       revenue - LAG(revenue) OVER (ORDER BY date) AS growth
FROM data;

-- Rolling Avg
SELECT date,
       AVG(revenue) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_revenue
FROM data;
