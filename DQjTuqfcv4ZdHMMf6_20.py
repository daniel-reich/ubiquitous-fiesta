
def getNumbers_list(num): 
    #This function will return the descending order of the numbers in a sequence 
    numList = [] 
    for _n in str(num): 
        numList.append(int(_n)) 
    return numList 
def minus(firstNum,secondNum): 
    diff = [] 
    for i in range(len(firstNum)): 
        diff.append(firstNum[i] - secondNum[i])
    return diff 
​
def convertListToNum(minusNums): 
    num = "" 
    for _mNums in minusNums: 
        num += str(_mNums) 
    return int(num)
def addExtraZero(diff): 
    #This function will add an extra zero to the number 
    return int('0' + str(diff))
def kaprekar(num,counter=1 ): 
    if num == 6174: 
        return 0 
    if num < 1000: 
        num *= 10
    smallNumber = convertListToNum(sorted(getNumbers_list(num)))
    bigNumber = convertListToNum(sorted(getNumbers_list(num),reverse = True))
    diff =bigNumber - smallNumber 
    #if diff < 1000: 
        #diff = addExtraZero(diff)
    
    if diff == 6174: 
        print(counter)
        return counter
    
    else:
        counter += 1
        return kaprekar(diff,counter)

