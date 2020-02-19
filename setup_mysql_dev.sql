-- Creates database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS dev_db;
USE dev_db;
CREATE USER IF NOT EXISTS 'dev'@'localhost';
SET PASSWORD FOR 'dev'@'localhost' = 'dev_pwd';
GRANT ALL PRIVILEGES ON dev_db.* TO 'dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'dev'@'localhost';
