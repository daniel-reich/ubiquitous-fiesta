
def is_pandigital(n):
    listNum = listNumbers(n)
    for n in range(10):
        for i in listNum:
            if n in listNum:
                break
            else:
                return False
    return True
​
def listNumbers(num):
    listNum = []
    strNum = str(abs(num))
    for i in strNum:
        listNum.append(int(i))
    return listNum

