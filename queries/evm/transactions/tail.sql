SELECT
    *
FROM
    ethereum.transactions t
WHERE
    block_number IS NOT NULL
    AND DATE(block_date) = CURRENT_DATE
ORDER BY
    block_number DESC
LIMIT 10