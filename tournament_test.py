# Test cases for tournament.py

from tournament import *


def testDelete():
    delete_Matches()
    delete_Players()
    print "b) Player's record can be deleted."


def testCount():
    delete_Matches()
    delete_Players()
    c = count_Players()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "c) CountPlayers() returns zero after deletion."


def testDeleteMatches():
    delete_Matches()
    print "a) Matches Occurred can be deleted."


def testReportMatches():
    delete_Matches()
    delete_Players()
    register_Player("Shalvi Saxena")
    register_Player("Shitij Tomar")
    register_Player("Sakshi Sikri")
    register_Player("Sharandeep Gotra")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_Match(id1, id2)
    report_Match(id3, id4)
    standings = playerStandings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each loser should have zero wins recorded.")
    print "g) After a match, players have updated standings."


def testRegisterCountDelete():
    delete_Matches()
    delete_Players()
    register_Player("Arnav Puri")
    register_Player("Anubhav Sharma")
    register_Player("Anuj Singla")
    register_Player("Arpit Dhal")
    c = count_Players()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    delete_Players()
    c = count_Players()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "e) Players can be registered and deleted."


def testStandingsBeforeMatches():
    delete_Matches()
    delete_Players()
    register_Player("Saloni Gupta")
    register_Player("Sakshi Jain")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even"
                         "before they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Saloni Gupta", "Sakshi Jain"]):
        raise ValueError("Registered players' names should appear in "
                         "standings, even if they have no matches played.")
    print "f) Newly registered players appear in the standings."


def testRegister():
    delete_Matches()
    delete_Players()
    register_Player("Chitra Sood")
    c = count_Players()
    if c != 1:
        raise ValueError(
            "After Registration of one player, countPlayers() should be 1.")
    print "d) After registering a player, countPlayers() returns 1."


def testPairings():
    delete_Matches()
    delete_Players()
    register_Player("Shefali Gautam")
    register_Player("Shivam Gupta")
    register_Player("Samiha Arya")
    register_Player("Stuti")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_Match(id1, id2)
    report_Match(id3, id4)
    pairings = swiss_Pairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "h) After one match, players with one win are paired."


if __name__ == '__main__':
    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"
