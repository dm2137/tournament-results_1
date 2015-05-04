#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

#Establish function to connect to the database named tournament
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

#Function to remove all records in the matches table
def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from matches")
    conn.commit()
    conn.close()

#Function to remove all records in the players table
def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from players")
    conn.commit()
    conn.close()

#Function that counts all the players in the tournament
def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("select count(*) as num from players")
    playercount = c.fetchall()[0][0]
    conn.close()
    return playercount
    
#Function that adds players to the database
#player names are cleaned using Bleach before committing to the database
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    cleancontent = bleach.clean(name)
    c.execute("insert into players (name) values (%s)", (cleancontent,))
    conn.commit()
    conn.close()

#Function that provides a table of player standings sorted in order by wins
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    query = '''
           SELECT players.player_ID, players.name,
             (select count(matches.winner) from matches
              where players.player_ID = matches.winner) as wins,
             (select count(matches.match_ID) from matches
              where players.player_ID in (matches.winner, matches.loser))
              as matches_played
           FROM players
           GROUP BY players.player_ID
           ORDER BY wins DESC
            '''
    c.execute(query)
    standings = c.fetchall()
    conn.close()
    return standings

#Function records the winner and losers of the match
#The input is cleaned using Bleach before committing to the DB
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    cleanwinner = bleach.clean(winner)
    cleanloser = bleach.clean(loser)
    c.execute("insert into matches (winner, loser) values (%s, %s)", (cleanwinner, cleanloser,))
    conn.commit()
    conn.close()

#Function pairs the players for the next round of matches
#All players are matched to an opponent of equal of similiar wins
# function creates a list and then returns a tuple with the data
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c = conn.cursor()
    standings = playerStandings()
 
    match_pairs = []
    next_pair = None
    for row in standings:
        if next_pair==None:
            next_pair = [row[0],row[1]]
            continue
  
        next_pair.append(row[0])
        next_pair.append(row[1])
 
        match_pairs.append(next_pair)
        next_pair = None
        
        match_tuple = tuple(match_pairs)
        
       
    conn.close()
    return match_tuple

