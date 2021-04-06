
def time_adjust(now,hrs, mins, sec):
    sol = ""
    hour = 0
    min = 0
    se = 0
    time = 0
    hour += int(now[0]) * 10
    hour += int(now[1])
    min += int(now[3]) * 10
    min += int(now[4])
    se += int(now[6]) * 10
    se += int(now[7])
    hour += hrs
    min += mins
    se += sec
​
    time += hour * 60 * 60
    time += min * 60
    time += se
    print(hour, min, se)
​
    time /= 60
    time /= 60
​
    ho = time// 1
    print(ho)
    re = time - ho
    re *= 60
    remin = re//1
    print(remin)
    rese = re - remin
    rese *= 60
    print(round(rese, 1))
    if round(rese, 1) == 60:
        remin += 1
        rese = 0
    for x in range(100):
        if ho >= 24 :
            ho -= 24
    print(ho, remin, round(rese, 1))
​
    if ho < 10:
        sol += "0"+str(int(ho))+":"
    else:
        sol += str(int(ho)) + ":"
    if remin < 10:
        sol += "0"+str(int(remin))+":"
    else:
        sol += str(int(remin)) + ":"
    if round(rese, 1) < 10:
        sol += "0"+str(int(round(rese, 1)))
    else:
        sol += str(int(round(rese, 1)))
    print(sol)
    
    return sol

