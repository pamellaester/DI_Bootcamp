-- create table Customer(
-- 	customer_id SERIAL,
--   first_name VARCHAR(50) ,
--   last_name VARCHAR(50) NOT NULL,
--   PRIMARY KEY (customer_id)
-- );

-- insert into customer (first_name,last_name) values 
--    ('John', 'Doe'),
--    ('Jerome', 'Lalu'),
--    ('Lea', 'Rive');
   
-- create table Customer_profile(
--   pk_customer_id INTEGER unique,
--   isLoggedIn boolean DEFAULT false,
--   PRIMARY KEY (pk_customer_id),
--   CONSTRAINT fk_customer_id FOREIGN KEY (pk_customer_id) REFERENCES customer(customer_id)
-- );

-- insert into customer_profile(pk_customer_id,isLoggedIn)
-- values
-- ((SELECT customer_id FROM customer where first_name = 'John'),'True'),
-- ((SELECT customer_id FROM customer where first_name = 'Jerome'),'False')
    

-- select customer.first_name from customer 
-- inner join customer_profile on customer.customer_id = customer_profile.pk_customer_id where customer_profile.isLoggedIn = true

-- create table books(
--   book_id SERIAL primary key,
--   title text not null ,
--   author VARCHAR(50) NOT NULL
-- );

-- insert into books (title,author)
-- values
--    ('Alice In Wonderland',' Lewis Carroll'),
--    ('Harry Potter', 'J.K Rowling'),
--    ('To kill a mockingbird', 'Harper Lee');
   
-- create table students(
--  student_id SERIAL primary key,
-- 	name varchar NOT NULL UNIQUE,
-- 	age int 
-- );

-- insert into students(name,age) 
-- values
--     ('John', '12'),
-- 	('Lera',' 11'),
-- 	('Patrick', '10'),
-- 	('Bob', '14');
	
-- CREATE TABLE libraries (
--   book_fk_id INTEGER NOT NULL,
--   student_fk_id INTEGER NOT NULL,
--   borrowed_date TIMESTAMP ,
--   PRIMARY KEY (book_fk_id, student_fk_id),
--   FOREIGN KEY (book_fk_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--   FOREIGN KEY (student_fk_id) REFERENCES students(student_id)ON DELETE CASCADE ON UPDATE CASCADE
-- );	

-- INSERT into libraries(student_fk_id, book_fk_id, borrowed_date) 
-- VALUES 
-- ((SELECT student_id FROM students where name = 'John'), 
-- (SELECT book_id FROM books where title = 'Alice In Wonderland'), '2022-02-15'),


-- INSERT into libraries(student_fk_id, book_fk_id, borrowed_date) 
-- VALUES 
-- ((SELECT student_id FROM students where name = 'Bob'), 
-- (SELECT book_id FROM books where title = 'To kill a mockingbird'), '2021-03-03'),

-- INSERT into libraries(student_fk_id, book_fk_id, borrowed_date) VALUES 
-- ((SELECT student_id FROM students where name = 'Lera'), 
-- (SELECT book_id FROM books where title = 'Alice In Wonderland'), '2021-05-23'),

-- INSERT into libraries(student_fk_id, book_fk_id, borrowed_date) VALUES 
-- ((SELECT student_id FROM students where name = 'Bob'), 
-- (SELECT book_id FROM books where title = 'Harry Potter'), '2021-08-12');

-- select * from libraries;

-- select students.name,books.title 
-- from students where libraries
-- join students on libraries.student_fk_id = students.student_id
-- join book on libraries.book_fk_id = books.book_id


