SELECT
    user_id,
    MAX(time_stamp) AS last_login
FROM login 
WHERE YEAR(time_stamp) = '2020'
GROUP BY user_id;