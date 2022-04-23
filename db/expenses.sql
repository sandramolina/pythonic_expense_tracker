DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS categories;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    merchant_id INT REFERENCES merchants(id),
    category_id INT REFERENCES categories(id),
    amount VARCHAR(255),
    description VARCHAR(255)
);