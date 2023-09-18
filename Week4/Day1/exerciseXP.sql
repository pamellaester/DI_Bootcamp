-- create a table
CREATE TABLE items (
id serial primary key,
item_name varchar,
price integer
);

INSERT INTO items (item_name,price)
 VALUES 
    ('Small Desk',  100),
    ('Large desk',  300),
    ('Fan',  80);


CREATE TABLE costumers (
id serial primary key,
first_name  varchar  ,
last_name varchar 
);


INSERT INTO costumers (first_name,last_name) 
 VALUES 
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor',' Green'),
    ('Melanie', 'Johnson');


SELECT * FROM items;
SELECT * FROM items where price > 80;
SELECT * FROM items where price <= 300;
SELECT * FROM costumers where last_name = 'Smith';
SELECT * FROM costumers where last_name = 'Jones';
SELECT * FROM costumers where first_name != 'Scott';



