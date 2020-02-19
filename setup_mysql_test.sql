-- Creates database hbnb_test_db
CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;
CREATE USER IF NOT EXISTS 'test'@'localhost';
SET PASSWORD FOR 'test'@'localhost' = 'test_pwd';
GRANT ALL PRIVILEGES ON test_db.* TO 'test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'test'@'localhost';
