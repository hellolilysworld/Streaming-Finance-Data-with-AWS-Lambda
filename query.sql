SELECT name,
         hour(cast(ts AS timestamp)) hour,
         max(high) max_high
FROM "17"
GROUP BY  name,hour(cast(ts AS timestamp))
ORDER BY  hour(cast(ts AS timestamp));