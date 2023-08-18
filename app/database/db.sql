CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL UNIQUE,
    user_email VARCHAR(255) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    CONSTRAINT valid_email CHECK(user_email ~* '^[a-zA-Z0-9.!#$%&''''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'),
    CONSTRAINT valid_password CHECK(LENGTH(user_password) >= 8)
);
CREATE TABLE IF NOT EXISTS posts(
    post_id SERIAL PRIMARY KEY,
    post_text VARCHAR(1023) NOT NULL,
    post_date_time TIMESTAMPTZ DEFAULT NOW(),
    post_votes INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT user_post FOREIGN KEY(user_id) REFERENCES users(user_id)
);