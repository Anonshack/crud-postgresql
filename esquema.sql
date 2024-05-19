CREATE TABLE pet(
	id serial primary key,
	name varchar(50) NOT NULL,
	age smallint NOT NULL
);

insert into pet
(name, age)
values
('pet_pet', 1),
