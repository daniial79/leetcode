WITH firstOrders AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_order
    FROM delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(
        SUM(
            IF(
                d.order_date = d.customer_pref_delivery_date, 
                1, 
                0
            )
        ) / COUNT(*)
        * 100, 2
    ) AS immediate_percentage
FROM 
    delivery d
JOIN
    firstOrders f
ON
    f.customer_id = d.customer_id
AND
    d.order_date = f.first_order;
