SELECT
    s.sales_id
FROM SalesPerson s 
WHERE s.sales_id NOT IN (
    SELECT 
        o.sales_id
    FROM Orders o 
    INNER JOIN Company c c.emp_id = o.emp_id
    WHERE c.name = "RED"
);