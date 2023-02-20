CREATE TABLE members (
	member_id VARCHAR ( 50 ) PRIMARY KEY UNIQUE NOT NULL,
	first_name VARCHAR ( 50 )  NOT NULL,
	last_name VARCHAR ( 50 )  NOT NULL,
	email VARCHAR ( 255 ) NOT NULL,
	phone VARCHAR ( 50 ) NOT NULL,
	above_18 BOOL NOT NULL
);

CREATE TABLE items (
	item_id int PRIMARY KEY UNIQUE NOT NULL,
	item_name VARCHAR ( 50 )  NOT NULL,
	manufacture_name VARCHAR ( 50 ) NOT NULL,
	weight_kg NUMERIC NOT NULL,
	cost int NOT NULL
);

CREATE TABLE transactions (
	transaction_id int NOT NULL,
	item_id int NOT NULL,
	quantity int NOT NULL,
  	total_price int NOT NULL,
	total_weight NUMERIC NOT NULL,
	transaction_datetime TIMESTAMP NOT NULL,
	member_id VARCHAR ( 50 ) NOT NULL,
	PRIMARY KEY (transaction_id, item_id),
  	CONSTRAINT fk_item_t FOREIGN KEY(item_id) REFERENCES items(item_id),
  	CONSTRAINT fk_members_t FOREIGN KEY(member_id) REFERENCES members(member_id)
);

COMMIT;
