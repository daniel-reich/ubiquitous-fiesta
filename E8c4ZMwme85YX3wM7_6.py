
def recaman(n):
        recamanList = []
        duplicatesList = []
        number = 0
        counter = 0
        
        while(len(recamanList) < n) :
                newNegNumber = number - counter
                newPosNumber = number + counter
                if recamanList.count(newNegNumber) == 0 and newNegNumber > 0:
                        recamanList.append(newNegNumber)
                        number = newNegNumber
                        counter += 1
                else:
                        recamanList.append(newPosNumber)
                        number = newPosNumber
                        counter += 1
                        
                if recamanList.count(number) > 1 and duplicatesList.count(number) == 0:
                        duplicatesList.append(number)
​
        output = "---> Recaman's sequence: {}\n---> Duplicates for n = {}: {}".format(recamanList, n, duplicatesList)
        return output

