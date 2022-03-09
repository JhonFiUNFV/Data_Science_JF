CREATE TABLE directors (
	director_id SERIAL PRIMARY KEY,
	first_name VARCHAR(150),
	last_name VARCHAR(150),
	date_of_birth DATE,
	nationality VARCHAR(20),
	add_date DATE,
	update_date DATE
);

SELECT * FROM directors;

-- Create the movies table 
CREATE TABLE movies(
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(100) NOT NULL,
	movie_length INT,
	movie_lang VARCHAR(20),
	age_certificate VARCHAR(10),
	release_date DATE,
	director_id INT REFERENCES directors(director_id)
);

-- Create a movies_revenues table
CREATE TABLE movies_revenues(
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies(movie_id),
	revenues_domestic NUMERIC (10,2),
	revenues_international NUMERIC (10,2)
);

SELECT * FROM movies_revenues;

-- Creating a movies_actors junction table
CREATE TABLE movies_actors(
	movie_id INT REFERENCES movies(movie_id),
	actor_id INT REFERENCES actors(actor_id),
	PRIMARY KEY (movie_id, actor_id)
);

SELECT * FROM movies_actors;

