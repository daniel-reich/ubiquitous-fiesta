
import math
def is_narcissistic(n):
    strN = str(n)
    sumAdd = 0
    for i in range(0,len(strN)):
        sumAdd += math.pow(int(strN[i]), len(strN))
    sumAdd = int(sumAdd)
    if (sumAdd == n):
        return True
    return False

