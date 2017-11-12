DROP SCHEMA IF EXISTS `MUSIC`;
CREATE SCHEMA IF NOT EXISTS `MUSIC`;
USE `MUSIC`;

-- Creating Table --

DROP TABLE IF EXISTS `Artist`;
DROP TABLE IF EXISTS `Album`; 
DROP TABLE IF EXISTS `Song`;

CREATE TABLE `Artist` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT
    );

CREATE TABLE `Album` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT,
    artist_id INT,
    FOREIGN KEY(artist_id) REFERENCES Artist(id)
    );

CREATE TABLE `Song` (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT,
    trackNumber INT,
    duration INT,
    album_id INT,
    FOREIGN KEY(album_id) REFERENCES Album(id)
	);