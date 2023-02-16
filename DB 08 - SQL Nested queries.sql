-- 문제 1
select 
	productcode , productname , msrp 
from
	products
where
	msrp > (select avg(msrp) from products) 
order by
	msrp asc;
-- 문제 2
select 
	customerNumber, customerName
from 
	customers
where
	customernumber in (SELECT customerNumber 
    from orders 
    where  orderdate 
    BETWEEN date('2003-01-06') and date('2003-03-27') )
order by
	customerNumber asc; 
-- 문제 3
SELECT
	productCode , productName , productLine , MSRP
from
	products
where
	productLine = 'classic cars'
	and msrp = (select max(msrp) from products) ;
-- 문제 4
select 
	customerNumber , customerName , country
from
	customers
where 
country = ( select MAX(country) from customers)
 order by
	customernumber asc;
-- 문제 5
select
	customerNumber , customerName , order_count
from
	customers
inner join ( select customernumber, count(customerNumber) as order_count
	from orders
    group by customernumber
    order by order_count desc
    limit 1
	) as sub using (customernumber)
ORDER BY order_count desc ;
-- 문제 6
select
	productCode , productName
from
	orderdetails
natural join products
where
	orderdate BETWEEN date('2004-01-01') and date('2005-01-01')
order by
	productCode desc;
--
SELECT customerNumber, COUNT(customerNumber) AS order_count
    FROM orders
    GROUP BY customerNumber
    ORDER BY order_count DESC
    LIMIT 2
--