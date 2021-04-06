
def bugger(num):
    newnum = num
    tsum = 1
    counter = 0
    while( newnum > 9 ):
        newnum = str(newnum)
        for i in range(len(newnum)):
            tsum = tsum * int(newnum[i])
        counter += 1
        newnum = tsum
        tsum = 1
    return counter

