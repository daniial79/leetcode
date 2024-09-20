SELECT
    customer_id
FROM customer
INNER JOIN product USING (product_key)
WHERE COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) FROM product
);