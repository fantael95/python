-- 자동 커밋 비활성화
set autocommit = 0 ;
--  
drop table users;
--
create table users(
	id int AUTO_INCREMENt,
    name VARCHAR(10) not null,
    primary key(id)
    );
-- 
start transaction;
insert into users (name)
values ('harry'), ('test');

select * from users
rollback;
select  * from users;
--
create table articles (
	id int auto_increment,
    title varchar(100) not null,
    createdat datetime not null,
    updatedat datetime not null,
    primary key(id)
    );
insert into articles (title, createdat, updatedat)
values ('title1' , current_time(),current_time()); 
--
delimiter //
create trigger beforearticleupdate
	before update
    on articles for each row
begin
	set NEW.updatedat = current_time();
end//
delimiter ;
--
insert into articles (title, createdat,updatedat)
values ('title2',current_time(),current_time());
select * from articles;
select * from articlelogs;
--
create table backuparticles (
	id int AUTO_INCREMENT,
    title varchar(100) not null,
    createdat datetime not null,
    updatedat datetime not null,
    primary key (id)
);
--
delimiter//
create trigger
	after delete
    on articles for each row
begin
	insert into backuparticles (title, createdat, updatedat)
	values(old.title,old.createdat,old.updatedat);
end//
delimiter;	
--