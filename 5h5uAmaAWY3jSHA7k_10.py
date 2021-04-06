
def landscape_type(landscape):
    highestval = landscape[0]
    highestvallocation = 0
    for i in range(0, len(landscape)):
        if highestval < landscape[i]:
            highestval = landscape[i]
            highestvallocation = i
​
    if highestvallocation != 0 and highestvallocation != len(landscape)-1:
        lowerhalf = landscape[ : highestvallocation]
        higherhalf = landscape[highestvallocation+1 : ]
        check = 0
​
        for i in range(0, len(lowerhalf) - 1):
            if lowerhalf[i] > lowerhalf[i+1]:
                check = 1
​
        for i in range(0, len(higherhalf) - 1):
            if higherhalf[i] < higherhalf[i+1]:
                check = 1
    else:
        check = 1
​
    if check == 0:
        return "mountain"
    else:
        lowestval = landscape[0]
        lowestvallocation = 0
        for i in range(0, len(landscape)):
            if lowestval > landscape[i]:
                lowestval = landscape[i]
                lowestvallocation = i
​
        if lowestvallocation != 0 and lowestvallocation != len(landscape)-1:
            lowerhalf = landscape[ : lowestvallocation]
            higherhalf = landscape[lowestvallocation+1 : ]
            check = 0
​
            for i in range(0, len(lowerhalf) - 1):
                if lowerhalf[i] < lowerhalf[i+1]:
                    check = 1
​
            for i in range(0, len(higherhalf) - 1):
                if higherhalf[i] > higherhalf[i+1]:
                    check = 1
        else:
            check = 1
​
        if check == 0:
            return "valley"
        else:
            return "neither"

