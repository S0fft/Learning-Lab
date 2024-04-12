CREATE TABLE users (
	id BIGINT NOT NULL PRIMARY KEY,
	first_name VARCHAR(64) NOT NULL,
	last_name VARCHAR(64) NOT NULL,
	email VARCHAR(128) NOT NULL
);

-- INSERT INTO users (id, first_name, last_name, email)
-- VALUES (1, 'Evgeniy', 'Pelikh', 'pelikh123.evg@gmail.com');
INSERT INTO users (id, first_name, last_name, email)
VALUES (2, 'Name1', 'Surname1', 'email1@gmail.com');

INSERT INTO users (id, first_name, last_name, email)
VALUES (3, 'Name2', 'Surname2', 'email2@gmail.com');

UPDATE users SET
email = 'newemail@gmail.com'
WHERE id = 	1;

DELETE FROM users
WHERE id = 2 or id = 3

SELECT id, first_name, last_name, email FROM users
WHERE id = 1;

CREATE TABLE spendings (
	id BIGINT NOT NULL PRIMARY KEY,
	price INT NOT NULL,
	created_at TIMESTAMP DEFAULT now(),
	user_id BIGINT NOT NULL,

	CONSTRAINT user_id_fk FOREIGN KEY(user_id) REFERENCES users (id)
);

INSERT INTO spendings (id, price, user_id)
VALUES (1, 78786, 3);

SELECT * FROM spendings
JOIN users ON users.id = spendings.user_id

SELECT spendings.*, users.first_name FROM spendings
INNER JOIN users ON users.id = spendings.user_id

SELECT spendings.*, users.first_name FROM spendings
RIGHT OUTER JOIN users ON users.id = spendings.user_id

SELECT spendings.*, users.first_name FROM spendings
LEFT OUTER JOIN users ON users.id = spendings.user_id

SELECT spendings.*, users.first_name FROM spendings
FULL OUTER JOIN users ON users.id = spendings.user_id

SELECT SUM(price) FROM spendings
GROUP BY user_id

SELECT users.*, SUM(spendings.price) FROM users
JOIN spendings ON users.id = spendings.user_id
GROUP BY users.id, spendings.user_id
HAVING SUM(spendings.price) > 1000000
-- WHERE SUM(spendings.price) > 1000000

ALTER TABLE spendings ADD COLUMN category_id BIGINT;
ALTER TABLE spendings ADD CONSTRAINT category_fk FOREIGN KEY (category_id) REFERENCES categories (id);