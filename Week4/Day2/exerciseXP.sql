-- select * from customer;
-- select first_name, last_name as full_name from customer;
-- select distinct create_date from customer ;
-- select * from customer order by first_name desc;
-- select film_id,title,description,release_year,rental_rate from film order by rental_rate asc;
-- select address, phone from address where district = 'Texas';
-- select * from film where rental_rate = (select min(rental_rate) from film) limit 10;
-- select * from film where rental_rate = (select min(rental_rate) from film) limit 10 offset 10 ;
-- select customer.first_name,customer.last_name,payment.amount,payment.payment_date
-- from customer 
-- inner join payment on customer.customer_id = payment.customer_id 
-- order by customer.customer_id;
-- select city.city, country.country
-- from city 
-- join country on city.country_id = country.country_id;







