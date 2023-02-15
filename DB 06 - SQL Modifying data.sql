-- 문제 1
create table users(
userId	int auto_increment,
first_name	varchar(20) not null,
last_name	varchar(20) not null,
birthday	date not null,
city	varchar(100),
country	varchar(100),
email	varchar(100),
created_at	datetime default 	CURRENT_TIMESTAMP,
primary key (userId)
);
-- 문제 2
INSERT into	users(first_name,last_name,birthday,city,country,email)
VALUES
('Beemo', 'Jeong', '1000-01-01',null,null,'beemo@hphk.kr'),
('Jieun','Lee','1993-05-16','Seoul','Korea',null),
('Dami','Kim','1995-04-09','Seoul','Korea',null),
('Kwangsoo','Lee','1985-07-14','Seoul','Korea',null) ;
-- 문제 3
INSERT into	users(first_name,last_name,birthday,city,country,email)
VALUES
('pin', ' ', '1000-01-01',' ',null,' '),
('Jake',' ','1991-01-11','Seoul','Korea',null),
('pb',' ','1901-02-01','Seoul','Korea',null),
('fp',' ','1991-02-14','Seoul','Korea',null) ;
-- 문제 4
update 
	users
set 
	first_name = 'taeyoung',
    last_name = 'lee',
    birthday = '1995-01-05'
where
	userid = 1;
-- 문제 5
update
	users
set 
	country = 'korea'
where
	country is null;
-- 문제 6
delete from users
where
	first_name = 'beemo';
-- 문제 7
delete from users
where
	first_name = 'Kwangsoo' and last_name = 'Lee';
--
delete from users
order by 
	created_at desc	
limit 1;
--
show COLUMNS from users;
--
select 
	*
from
	users;
--