
def swapPositions(list, pos1, pos2): 
    list[pos1],list[pos2] = list[pos2],list[pos1] 
    return list
​
def number_of_swaps(listOfNumbers):
    currentNumber = 0
    nextNumber = 0
    count = 1
    organizedListOfNumbers = []
    numberOfSwaps = 0
    for i in listOfNumbers:
        organizedListOfNumbers.append(i)
    organizedListOfNumbers.sort()
    while listOfNumbers != organizedListOfNumbers:
        for i in listOfNumbers:
            currentNumber = i
            indexOfCurrentNumber = listOfNumbers.index(i)
            if listOfNumbers.index(currentNumber) != len(listOfNumbers)-1:
                nextNumber = listOfNumbers[indexOfCurrentNumber+1]
                indexOfNextNumber = listOfNumbers.index(nextNumber)
                if count%2 == 1:
                    if currentNumber > nextNumber:
                        swapPositions(listOfNumbers, indexOfCurrentNumber, indexOfNextNumber)
                        numberOfSwaps += 1
                elif count%2 == 0:
                    if currentNumber < nextNumber:
                        swapPositions(listOfNumbers, indexOfCurrentNumber, indexOfNextNumber)
                        numberOfSwaps += 1
    return numberOfSwaps

