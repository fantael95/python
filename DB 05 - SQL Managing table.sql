-- 문제 1
CREATE table posts ( 
	postid int auto_increment not NULL ,
    title varchar(50) not NULL ,
    content	varchar(200) not null,
    primary key (postid)
    );
-- 문제 2
ALTER table 
	posts
add
	writer varchar(100) DEFAULT 'Anonymous' ,
add
	created_at	datetime DEFAULT CURRENT_TIMESTAMP() ;	
-- 문제 3
alter table
	posts
modify
	content text ;
-- 문제 4
alter table
	posts
drop
	writer ;
-- 문제 5
drop table
	posts;
-- 문제 6
create table if not EXISTS posts(
postId	int auto_increment,
title	varchar(50) not null,
content	text ,
writer	varchar(20),
created_at	datetime default CURRENT_TIMESTAMP,
PRIMARY key (postId)
);
-- 문제 7
drop table if exists posts ;
--
show columns from posts ;
--