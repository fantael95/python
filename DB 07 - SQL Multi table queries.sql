-- 문제 1
select
	employeeNumber, lastName, firstName, city
from
	employees
inner join offices
	on employees.officeCode = offices.officeCode
order by
	employeeNumber asc ;
-- 문제 2
select 
	customerNumber ,
    officeCode , 
    customers.city,
    offices.city
from
	customers
left join offices
	on offices.city = customers.city
order by
	customerNumber desc;
-- 문제 3
select
	customerNumber ,
    officeCode , 
    customers.city,
    offices.city
from
	customers
right join offices
	on offices.city = customers.city
order by
	customerNumber desc;
-- 문제 4
select
	customerNumber ,
    officeCode , 
    customers.city,
    offices.city
from
	customers
inner join offices
	on offices.city = customers.city
order by
	customerNumber desc;
-- 문제 5
-- 문제 2는 customer + customers와 일치하는 offices table 의 내용
-- 문제 3은 offices +  offices와 일치하는 customers table의 내용
-- 문제 4는 두 테이블에서 일치하는 부분만 표시하기 때문이다.
-- 문제 6
select
	customerNumber , officeCode , customers.city, offices.city
from
	customers
left join offices
	on offices.city = customers.city
union
select
	customerNumber , officeCode , customers.city, offices.city
from
	customers
right join offices
	on offices.city = customers.city
order by
	customerNumber desc;
-- 문제7
select 
	orders.orderNumber,
    orderDate
from
	orderdetails
inner join orders
ORDER BY
	ordernumber asc;
-- 문제 8
select 
	orderNumber , products.productCode , productName
from
	orderdetails
inner join products
	on products.productCode = orderdetails.productCode 
order by
	orderNumber asc;
-- 문제 9
select 
	orderNumber , productCode , orderDate, productName
from
	orderdetails
NATURAL join orders
NATURAL join products 
order by
	orderNumber asc;
--