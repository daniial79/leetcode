SELECT
    u.name
    SUM(t.amount) AS balance
FROM users u 
JOIN transactions t USING (account)
HAVING balance > 10000;