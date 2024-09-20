-- solution 1
SELECT IFNULL(
    (SELECT num
    FROM (
        SELECT 
            num
        FROM MyNumbers
        GROUP BY num
        HAVING COUNT (num) = 1
        ORDER BY num DESC LIMIT 1
    ) derived_table),
    NULL
) AS "num";

-- solution 2
WITH CTE AS (
    SELECT 
        num 
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
    ORDER BY num DESC LIMIT 1
);

SELECT MAX(num) AS "num" FROM CTE;