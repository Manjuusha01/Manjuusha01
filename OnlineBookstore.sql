create database OnlineBookstore;
use OnlineBookstore;

create table books (
book_id int primary key,
title varchar(50),
author_id int,
price decimal(10,2),
publication_year year
);

create table authors (
author_id int primary key,
author_name varchar(25),
country varchar(20)
);

create table orders (
order_id int primary key,
book_id int,
customer_name varchar(30),
order_date date
);

insert into books
values(101,'Harry Potter',1,1000.00,2006);
insert into books
values(102,'Two States',2,750.00,2012);
insert into books
values(103,'Alchemist',3,680.00,2010);

select * from books

insert into authors
values(11,'J.K Rowling','England');
insert into authors
values(12,'Chetan Bhagath','India');
insert into authors
values(13,'Paulo Koehlo','Brazil');

insert into orders
values(234,102,'Sajitha','2020-06-12');
insert into orders
values(657,103,'Ardra','2022-10-26');
insert into orders
values(938,102,'Manjusha','2023-11-04');

select * from books;
select * from authors;
select * from orders;

alter table books add column genre varchar(50);

alter table orders add column quantity int;
authors

select b.title, b.genre, b.price, b.publication_year, a.author_name, a.country
from books b
join authors a on b.author_id = a.author_id;

select o.order_id, b.title as book_title, o.customer_name, o.order_date, o.quantity
from orders o
join books b on o.book_id = b.book_id;


