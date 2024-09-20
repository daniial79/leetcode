WITH BoardinQueue AS (
    SELECT
        person_id,
        person_name,
        weight,
        turn
        SUM(weight) OVER(ORDER BY turn) AS cumulative_weight
)
SELECT 
    person_name
FROM BoardingQueue
WHERE cumulative_weight <= 100
ORDER BY cumulative_weight DESC
LIMIT 1;