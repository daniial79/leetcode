SELECT
    user_id AS id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS user_id 
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS user_id
    FROM RequestAccepted
) AS Combined
GROUP BY id
ORDER BY num DESC LIMIT 1;

-- more general way
WITH FriendsNumberCTE AS (
    SELECT
        user_id,
        COUNT(*) AS friends
    FROM (
        SELECT requester_id AS user_id 
        FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS user_id
        FROM RequestAccepted
    ) C
    GROUP BY user_id
    ORDER BY friends DESC
)

SELECT 
    user_id AS id,
    friends AS num
FROM FriendsNumberCTE
WHERE friends = (
    SELECT MAX(friends) FROM FriendsNumberCTE
);