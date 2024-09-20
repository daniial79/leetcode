SELECT 
    p.product_name
    SUM(o.order_date) AS unit
FROM products p 
INNER JOIN orders o USING (product_id)
WHERE YEAR(o.order_date) = "2020" AND MONTH(o.order_date) = "02"
GROUP BY p.product_name
HAVING unit >= 100