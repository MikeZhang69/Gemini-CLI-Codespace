-- init.sql

-- Create a test user
-- Password is 'password'
INSERT INTO "user" (email, password_hash, base_currency, time_zone) VALUES
('test@example.com', '$2b$10$f.8.L9Q9.jH9.L9Q9.jH9.uL9Q9.jH9.L9Q9.jH9.L9Q9.j', 'USD', 'UTC');

-- Create a sample portfolio for the test user
INSERT INTO "portfolio" (name, "userId") VALUES
('My Sample Portfolio', 1);
