SELECT
    *
FROM
    ethereum.blocks b
WHERE
    number IS NOT NULL
    AND DATE(date) = CURRENT_DATE
ORDER BY
    number DESC
LIMIT 10