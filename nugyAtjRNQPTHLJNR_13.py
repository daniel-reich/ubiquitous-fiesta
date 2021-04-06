
def pages_in_book(total):
    isTrue = True
    arr = [i for i in range(1,total+1)]
    runningTotal = 0
    arr2 = []
    for i in arr:
        runningTotal = runningTotal +i
        arr2.append(runningTotal)
    # print(arr2)
    if total in arr2:
        return isTrue
    else:
        return not isTrue

