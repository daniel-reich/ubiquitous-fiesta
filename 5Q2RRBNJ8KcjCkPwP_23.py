
def tic_tac_toe(bd):
    d = {'X':'1', 'O':'2'}
    lor = []
    for row in bd:
        lor.append(row)
    tbd = map(list, zip(*bd))
    for row in tbd:
        lor.append(row)
    lor.append([bd[0][0], bd[1][1], bd[2][2]])
    lor.append([bd[0][2], bd[1][1], bd[2][0]])
    
    for row in lor:
        if row[0] == row[1] == row[2]:
            return 'Player ' + d[row[0]] + ' wins'
    return "It's a Tie"

