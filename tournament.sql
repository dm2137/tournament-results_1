-- Table definitions for the tournament project.
--
-- SQL 'create table' statements in this file
-- to create a table for the tournament players
-- and to create a table for the winners and losers of a paired match



--creates the table of players
create table players
   (player_ID serial PRIMARY KEY NOT NULL,
    name varchar(255)
   );

--creates the table of matches that identifies the winner and loser of the match
create table matches
   (match_ID serial PRIMARY KEY,
    winner int references players,
    loser int references players
    );

