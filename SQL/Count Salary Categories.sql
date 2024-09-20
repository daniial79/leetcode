SELECT 'Low Salary' AS category, IFNULL(SUM(income < 20000), 0) AS accounts_count FROM Accounts
UNION
SELECT
    'Average Salary' AS category,
    IFNULL(SUM(income BETWEEN 20000 AND 50000), 0) AS accounts_count
FROM Accounts
UNION
SELECT 'High Salary' AS category, IFNULL(SUM(income > 50000), 0) AS accounts_count FROM Accounts;


SELECT
    "Low Salary" AS category,
    SUM(CASE WHEN income < 20000 THEN 1 ELSE 0 END) AS accounts_count
FROM accounts
UNION ALL
SELECT
    "Average Salary" AS category,
    SUM(CASE WHEN income >= 20000 and income <= 50000 THEN 1 ELSE 0 END) AS accounts_count
FROM accounts
UNION ALL
SELECT
    "High Salary" AS category,
    SUM(CASE WHEN income > 50000 THEN 1 ELSE 0 END) AS accounts_count
FROM accounts
