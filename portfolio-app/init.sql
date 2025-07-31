-- init.sql

-- Create a test user
-- Password is 'password'
INSERT INTO "user" (email, password_hash, base_currency, time_zone) VALUES
('test@example.com', '$2b$10$Rmbhf9sdIi/atGoXyOyz5OLMy.H7JkoSlWEazp82Zm0f.6hKnxFxS', 'USD', 'UTC');

-- Create a sample portfolio for the test user
INSERT INTO "portfolio" (name, "userId") VALUES
('My Sample Portfolio', 1);
