-- 문제 1
select distinct
	country
from
	customers 
order by
	country asc ;
-- 문제 2
select distinct
	state 
from
	customers
order by
	state desc ;
-- 문제 3
select 
	customerNumber , customerName , country
from 
	customers
where
	country != 'usa'
order by 
	customerNumber desc ;
-- 문제 4
SELECT
	*
from
	offices
where
	city = 'paris' ;
-- 문제 5
select
	*
from 
	customers
where 
	country = 'usa' and state = 'ca' 
order by
	customerNumber desc ;    
-- 문제 6
select 
	customerNumber , customerName , country , state
from 
	customers
where
	country = 'usa' and state = 'ca' or  state = 'ny'
order by
	customerNumber desc ;
-- 문제 7
select 
	customerNumber , customerName , state
from 
	customers
where
	state = 'ca' or state = 'ny' or state = 'ct' or state = 'pa' 
order by
	customerNumber desc ; 
-- 문제 8
select 
	productCode , productName , quantityInStock
from 
	products
where
	quantityInStock < 1000 
ORDER BY 
	quantityInStock asc ;
-- 문제 9
select 
	productCode , productName , quantityInStock
from 
	products 
where
	quantityInStock <= 3000 and quantityInStock > 2000 
order by
	quantityInStock DESC ;
-- 문제 10
select 
	customerNumber , customerName , phone
from
	customers 
where
	phone like '%555' 
order by 
	customerName desc ;
-- 문제 11
select 
	productCode , quantityInStock
from 
	products
order by 
	quantityInStock desc 
limit 
	5 ;
-- 문제 12 
select 
	jobtitle, count(*)
from 
	employees
group by 
	jobtitle 
order by
	count(*) desc , jobtitle desc ;
-- 문제 13
select
	country, count(*) 'count_country'
from
	customers
group by
	country
order by
	country desc ;
-- 문제 14 
select
	orderNumber , sum(quantityOrdered * priceEach) as 'total'
from 
	orderdetails
GROUP BY
	orderNumber
ORDER BY
	total desc ;
-- 문제 15
select
	Year(orderDate) as year, count(orderNumber)
from 
	orders
group by 
	year(orderDate);
-- 문제 16
select
	productLine,  max(quantityInStock) 'max_stock'
from 
	products
group by
	productLine
having
	max(quantityInStock) < 9000 ;
-- 문제 17
SELECT
    ordernumber,
    SUM(quantityOrdered) AS itemsCount,
    SUM(priceeach * quantityOrdered) AS total
FROM
    orderdetails   
GROUP BY
    ordernumber
HAVING
    itemsCount >= 500 AND total >= 50000;

	