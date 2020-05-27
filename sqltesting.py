import sqlite3
import pprint
conn = sqlite3.connect('LCS_2020SpringMatchData.sqlite')
c = conn.cursor()

def player_result_array(tupleList):
    wins ={}
    losses ={}
    for tup in tupleList:
        if tup[1] == '1':
            if tup[0] not in wins.keys():
                wins[tup[0]] = 1
            else:
                wins[tup[0]] += 1
        else:
            if tup[0] not in losses.keys():
                losses[tup[0]] = 1
            else:
                losses[tup[0]]+=1
    #print ("Win Champ Dict", wins)
    #print ("Loss Champ Dict", losses)

    return {"wins":wins, "Losses":losses}

topLanerTupleList = c.execute('SELECT DISTINCT player FROM LCS_2020SpringMatchData where position="top" ').fetchall()
topLanerList = [item for t in topLanerTupleList for item in t] #https://www.geeksforgeeks.org/python-convert-list-of-tuples-into-list/
#print("topLaners", topLanerList)

topLanerStats = {}
for player in topLanerList:
    playerTuples = c.execute('SELECT champion, wins FROM LCS_2020SpringMatchData WHERE player=?', (player,)).fetchall()

    playerChampions = player_result_array(playerTuples)
    print(player, playerChampions)
    topLanerStats[player] = playerChampions

        

