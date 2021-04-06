
def EPLResult(table, team):
    season = sorted(table,key = lambda x: (x[2] * 3 + x[3],x[5]),reverse = 1)
    pos = [season.index(i) for i in season if team in i][0]
    won,draw,diff = season[pos][2] * 3,season[pos][3],season[pos][5]
    suffix = ['th','st', 'nd', 'rd', 'th'][min(pos + 1 % 10,4)]   
    return "{} came {}{} with {} points and a goal difference of {}!".format(team,pos + 1,suffix,won + draw,diff)

