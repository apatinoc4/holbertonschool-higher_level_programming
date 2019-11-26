-- Create database hbtn usa and States table inside of it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(256) NOT NULL
);