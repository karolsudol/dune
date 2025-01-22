SELECT
    block_date,
    "from" as sender, 
    COUNT(*) as txs_cnt
FROM
    ethereum.transactions
WHERE
    DATE(block_date) BETWEEN DATE '{{StartDate}}' AND DATE '{{EndDate}}'
    AND LOWER(CAST("from" AS varchar)) IN (
        SELECT LOWER(sender_address) 
        FROM UNNEST(SPLIT('{{TransactionSenders}}', ',')) AS s(sender_address)
    )
GROUP BY
    1,2
ORDER BY
    1 DESC, 3 DESC