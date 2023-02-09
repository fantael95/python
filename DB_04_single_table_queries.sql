-- 문제 1
select 
	*
from
	employees ;
-- 문제 2
SELECT
	customerNumber , customerName , phone
from
	customers ;
-- 문제3 
select
	firstName , lastName , email
from 
	employees 
ORDER BY
	firstName ASC;
-- 문제 4
select
	firstName as '이름' , lastName as '성', email as '이메일'
from 
	employees
ORDER BY
	이름 asc ;
-- 문제5
select
	employeeNumber , lastName , firstName , officeCode , jobTitle
from
	employees
ORDER BY
	jobTitle DESC , officeCode asc ;
-- 문제 6
select
	*
from	
	orderdetails
order by
	quantityOrdered asc , priceEach desc ;
-- 문제 7
select
	customerNumber , country , contactFirstName
from
	customers
order by
	country asc , contactFirstName desc ;
-- 문제 8
SELECT
	productCode , quantityInStock , buyPrice, quantityInStock*buyPrice
from
	products
ORDER BY
	quantityInStock*buyPrice DESC ;