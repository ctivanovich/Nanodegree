SELECT sub3.rep_name, sub2.max_total
FROM
   (SELECT sub1.region as region, MAX(sub1.total_usd) as
   max_total
   FROM
    (SELECT s.name rep_name, r.name region,
     sum(o.total_amt_usd) total_usd
    from sales_reps s
    JOIN region r ON s.region_id = r.id
    JOIN accounts a ON a.sales_rep_id = s.id
    JOIN orders o ON o.account_id = a.id
    GROUP BY r.name, s.name) sub1
  GROUP BY sub1.region) sub2
  JOIN
    (SELECT s.name rep_name, r.name region,
     sum(o.total_amt_usd) total_usd
    from sales_reps s
    JOIN region r ON s.region_id = r.id
    JOIN accounts a ON a.sales_rep_id = s.id
    JOIN orders o ON o.account_id = a.id
    GROUP BY r.name, s.name) sub3
ON sub3.region = sub2.region AND sub3.total_usd = sub2.max_total
