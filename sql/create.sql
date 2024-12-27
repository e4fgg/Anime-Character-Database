-- Creates
CREATE DATABASE AnimeCharacters;
CREATE SCHEMA IF NOT EXISTS UserCharacters;

-- Drops
DROP SCHEMA usercharacters;
DROP TABLE USERCHARACTERS.characters;

-- Creating table of the characters that will be inserted into the database.
CREATE TABLE IF NOT EXISTS usercharacters.characters(
	CharacterID SERIAL PRIMARY KEY NOT NULL,
	EnglishName VARCHAR(50) NOT NULL,
	JapaneseName VARCHAR(50) NOT NULL,
	Birthday DATE NOT NULL,
	Anime VARCHAR(75) NOT NULL
);

-- Using a select statement to check if program worked.
SELECT * 
FROM usercharacters.CHARACTERS;
