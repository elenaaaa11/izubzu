DROP TABLE IF EXISTS rent_history;
DROP TABLE IF EXISTS house_info;
DROP TABLE IF EXISTS area_info;
DROP TABLE IF EXISTS user_info;

/*
Create tables for database
*/

CREATE TABLE IF NOT EXISTS user_info (
	user_name VARCHAR(32) NOT NULL,
	real_name VARCHAR(32) NOT NULL,
	password VARCHAR(16) NOT NULL CHECK (LENGTH(password) >= 6),
	phone_number VARCHAR(16) UNIQUE NOT NULL,
	email VARCHAR(64) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS area_info (
	all_area VARCHAR(32) PRIMARY KEY
);


CREATE TABLE IF NOT EXISTS house_info (
	house_title VARCHAR(128) PRIMARY KEY,
	area VARCHAR(32) NOT NULL REFERENCES area_info(all_area)
	ON UPDATE CASCADE ON DELETE CASCADE,
	room_size INT NOT NULL,
	house_location VARCHAR(128) NOT NULL,
	postal_code VARCHAR(6) NOT NULL,
	number_of_bedrooms INT NOT NULL,
	number_of_washrooms INT NOT NULL,
	max_tenant INT NOT NULL,
	available_date DATE NOT NULL,
	expected_price DECIMAL(10,2) NOT NULL CHECK (expected_price>0),
	price_per_feet DECIMAL(6,2) NOT NULL CHECK (price_per_feet>0),
	negotiable VARCHAR(4) NOT NULL CHECK (negotiable='YES' OR negotiable='NO'),
	owner_email VARCHAR(64) NOT NULL REFERENCES user_info(email)
	ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE,
	owner_phone_number VARCHAR(16) NOT NULL REFERENCES user_info(phone_number)
	ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE,
	house_status VARCHAR(16) CHECK (house_status='FOR RENT' OR house_status='RENTED')
);

CREATE TABLE IF NOT EXISTS rent_history(
	borrower_email VARCHAR(64) NOT NULL REFERENCES user_info(email)
	ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE,
	owner_email VARCHAR(64) NOT NULL REFERENCES user_info(email)
	ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE,
	house_title VARCHAR(128) NOT NULL REFERENCES house_info(house_title)
	ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE,
	rent_price DECIMAL(10,2) NOT NULL CHECK (rent_price > 0),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	status VARCHAR(16) CHECK (status = 'SUCCESS' OR status = 'CANCELED'),
	PRIMARY KEY (borrower_email,owner_email, house_title, start_date)
);
