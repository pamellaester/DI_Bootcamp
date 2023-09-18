CREATE TABLE students (
id INTEGER PRIMARY KEY,
last_name VARCHAR NOT NULL,
first_name VARCHAR NOT NULL,
birth_date TIMESTAMP NOT NULL
);

INSERT INTO students (last_name,first_name,birth_date)
VALUES 
    ('Marc',	'Benichou',	    '02/11/1998'),
    ('Yoan',    'Cohen',	   ' 03/12/2010'),
    ('Lea', 	'Benichou',  	'27/07/1987'),
    ('Amelia',	'Dux',	        '07/04/1996'),
    ('David',	'Grez',	        '14/06/2003'),
    ('Omer',	'Simpson',      '03/10/1980');


SELECT * FROM students;
SELECT first_name,last_name FROM students;
SELECT first_name,last_name FROM students WHERE id = 2;
SELECT first_name,last_name FROM students WHERE first_name = 'Marc' OR last_name = 'Benichou';
SELECT first_name,last_name FROM students WHERE first_name LIKE'%a%';
SELECT first_name,last_name FROM students WHERE first_name LIKE'a%';
SELECT first_name,last_name FROM students WHERE first_name LIKE'%a';
SELECT first_name,last_name FROM students WHERE first_name LIKE'%_a%';
SELECT first_name,last_name FROM students WHERE id = 1 AND id = 3 ;
SELECT * FROM students WHERE birth_date >= '1/01/2000';


SELECT first_name,last_name,birth_date FROM students ORDER BY last_name ASC LIMIT 4; 
SELECT first_name,last_name,birth_date FROM students WHERE birth_date = (select MIN(birth_date) from students); 
SELECT first_name,last_name,birth_date FROM students WHERE id > 2 LIMIT 3;
    