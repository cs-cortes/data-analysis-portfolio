SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COALESCE(SUM(o.total_price), 0) AS total_spent,
    CASE
        WHEN COALESCE(SUM(o.total_price), 0) >= 7000 THEN 'Alto'
        WHEN COALESCE(SUM(o.total_price), 0) >= 3000 THEN 'Medio'
        ELSE 'Bajo'
    END AS customer_segment
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC;