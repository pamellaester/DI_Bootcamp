-- select * from language;
-- select film.title,film.description,language.name from film left join language on film.language_id = language.language_id;
-- select film.title,film.description,language.name from film inner join language on film.language_id = language.language_id;
-- select * from language left join film on film.language_id = language.language_id;
-- create table new_film ( 
-- id serial primary key,
-- name varchar (100)
-- );

-- select * from new_film;

-- create table customer_review (
--     review_id serial primary key not null,
-- 	film_id int not null,
-- 	language_id int not null,
-- 	title varchar (100) not null,
-- 	score int not null,
-- 	review_text text,
-- 	lat_update timestamp default current_timestamp,
	
-- 	constraint fk_language_id foreign key language_id references language(language_id),
-- 	constraint fk_film_id foreign key film_id references new_film(id),
-- 	constraint score_value check (score. 0 and score <= 10)
-- )

-- select * from new_film
-- insert into customer_reviews(film_id,langague_id,title,score,review_text) 
-- values
-- (1,1,"great movie",10,"the first movie i saw when i was a kid"),
-- (4,1,"not good",9,"i like it") returning * 

-- update film set language_id=2 where (title = 'Chamber Italian');
-- select * from customer where (fisrt_name = 'Ben');
-- insert into customer( first_name,last_name,store_id,address_id)
-- values 
-- ('Ben','Merjen',1,1);
-- drop table customer_reviews;
-- select * from rental where (return_date is null);
-- select * from rental
-- inner join inventory on rental.inventory_id = inventory.inventory_id
-- left join film on film_id = film.film_id 
-- where rental.return_date is null
-- order by film.replacement_cost desc
-- limit 30;
-- select film.film_id,dilm.title,film.fulltext from film_actor 
-- inner join film on film.film_id = film_actor.film_id
-- where (actor_id = (
-- 	select actor_id from actor where (first_name = 'Penelope' and last_name = 'monroe')						   
--     and film.fulltext @@ to to_tsquery ('english','sumo')
-- ))

-- select * from inventory
-- inner join film on film.film_id = inventory.film_id
-- inner join rental on rental.inventory_id = inventory.inventory_id
-- inner join customer on customer.customer_id = rental.customer_id
-- where customer.fist_name = 'Matthew'
-- and customer.last_name = 'Mahan'
-- and (film.title like '%Boat%' or film.description like '%Boat%')
-- order by film.replacement_cost desc