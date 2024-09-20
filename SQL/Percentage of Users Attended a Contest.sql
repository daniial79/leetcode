SELECT
    r.contest_id,
    ROUND(COUNT(r.user_id) * 100 / (SELECT COUNT(user_id) FROM users), 2) AS percentage
FROM register r
GROUP BY r.contest_id
ORDER BY 2 DESC, 1 ASC; 