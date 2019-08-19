CREATE TYPE plant_type AS ENUM ('flower', 'foliage', 'tree', 'shrub', 'ground_cover');
CREATE TYPE climate_type AS ENUM ('dry', 'tropical', 'temperate', 'continental', 'polar');
CREATE TABLE plant (
	id		SERIAL PRIMARY KEY,
	common_name	TEXT NOT NULL,
	scientific_name	TEXT NOT NULL,
	type_of_plant	plant_type NOT NULL
);
CREATE TABLE soil (
	id	SERIAL PRIMARY KEY,
	color	TEXT NOT NULL,
	acidity	DECIMAL DEFAULT 7.0,
	climate climate_type NOT NULL
);
CREATE TABLE bed (
	id	SERIAL PRIMARY KEY,
	plant	INTEGER REFERENCES plant(id),
	soil	INTEGER REFERENCES soil(id)
);