-- Create a table to store user data
CREATE TABLE users (
    id INTEGER PRIMARY KEY,  -- Unique identifier for each user
    name TEXT NOT NULL,      -- User's name (cannot be null)
    age INTEGER NOT NULL     -- User's age (cannot be null)
);

-- Insert data into the users table
INSERT INTO users (name, age) VALUES ('Alice', 30);   -- Inserting Alice's data
INSERT INTO users (name, age) VALUES ('Bob', 25);     -- Inserting Bob's data
INSERT INTO users (name, age) VALUES ('Charlie', 35); -- Inserting Charlie's data

-- Query the database to retrieve users older than 28
SELECT * FROM users WHERE age > 28;
