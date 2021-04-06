
def magic_square_game(aliceList,bobList):
​
    intersec = (bobList[0],aliceList[0])
​
    if (aliceList[1][intersec[0]-1]!=bobList[1][intersec[1]-1]):
        return False
    if (aliceList[1].count("0")!=1 and bobList[1].count("1")==2):
        return True
    else:
        return False

