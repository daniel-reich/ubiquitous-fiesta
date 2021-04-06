
def EPLResult(table, team):
    tab1 = [(i[0] + "*" + str(i[2] * 3 + i[3] * 1 + i[5]) + "*" + str(i[5])).split("*") for i in table]
    v = ""
    x = lambda a: int(a[1])
    tab1.sort(key=x, reverse=True)
    for i in range(len(tab1)):
        if tab1[i][0] == team:
            x = i
            break
    if x == 0:
        v = tab1[x][0] + " came 1st with " + str(
            int(tab1[x][1]) - int(tab1[x][2])) + " points and a goal difference of " + tab1[x][
                2] + "!"
    elif x == 1:
        v = tab1[x][0] + " came 2nd with " + str(
            int(tab1[x][1]) - int(tab1[x][2])) + " points and a goal difference of " + tab1[x][
                2] + "!"
    elif x == 2:
        v = tab1[x][0] + " came 3rd with " + str(
            int(tab1[x][1]) - int(tab1[x][2])) + " points and a goal difference of " + tab1[x][
                2] + "!"
    else:
        v = tab1[x][0] + " came " + str(x+1) + "th with " + str(
            int(tab1[x][1]) - int(tab1[x][2])) + " points and a goal difference of " + tab1[x][
                2] + "!"
    return v

