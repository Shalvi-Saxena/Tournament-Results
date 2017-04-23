# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def delete_Matches():
    """Remove all the match records."""
    DB = connect()
    curs = DB.cursor()
    curs.execute("delete from games;")
    DB.commit()
    DB.close()


def connect():
    """Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def report_Match(winner, loser):
    """Records the outcome of a single match between two players."""
    DB = connect()
    curs = DB.cursor()
    curs.execute("insert into games values (%s,%s);", (winner, loser))
    DB.commit()
    DB.close()


def count_Players():
    """Returns number of players currently registered."""
    DB = connect()
    curs = DB.cursor()
    curs.execute("select count(*) from players;")
    num = curs.fetchone()
    DB.close()
    return num[0]


def register_Player(name):
    """Adds a player to the tournament database."""
    DB = connect()
    curs = DB.cursor()
    curs.execute("insert into players values (%s);", (name,))
    DB.commit()
    DB.close()


def delete_Players():
    """Remove all the player records."""
    DB = connect()
    curs = DB.cursor()
    curs.execute("delete from players;")
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins."""
    DB = connect()
    curs = DB.cursor()
    curs.execute("select * from standings;")
    standings = curs.fetchall()
    DB.close()
    return standings


def swiss_Pairings():
    """Returns a list of pairs of players for the next round of a match."""
    standings = playerStandings()
    return [(standings[i-1][0], standings[i-1][1], standings[i][0],
            standings[i][1])
            for i in range(1, len(standings), 2)]
