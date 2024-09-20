SELECT
    p.product_id,
    IFNULL(ROUND(SUM(p.price * us.units) / SUM(us.units), 2), 0) AS average_price
FROM 
    Prices p
LEFT JOIN 
    UnitsSold us ON us.product_id = p.product_id AND
    us.purchase_date >= p.start_date AND 
    us.purchase_date <=  p.end_date
GROUP BY p.product_id;