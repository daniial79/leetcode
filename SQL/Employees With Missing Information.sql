SELECT T.employee_id
FROM (
    SELECT * FROM employees LEFT JOIN salaries USING (employee_id)
    UNION
    SELECT * FROM salaries LEFT JOIN employees USING (employee_id)
) AS T
WHERE T.salary IS NULL
ORDER BY T.employee_id;


WITH cte1 AS (
    SELECT * FROM employees e
    LEFT JOIN salaries s USING (employee_id)
    UNION
    SELECT * FROM employees e
    RIGHT JOIN salaries s USING (employee_id)
)

SELECT employee_id FROM cte1 
WHERE salary IS NULL
ORDER BY 1 ASC;