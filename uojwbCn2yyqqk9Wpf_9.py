
import math
def pdiv(n,number):
    p = 0
    i = 2
    while i <= (math.sqrt(n)) :
        if (n % i == 0) :
            if (i == (n / i)) :
                p += i;
            else :
                p += (i + n/i);
        i = i + 1
    return p + 1
​
def is_untouchable(number):
    myans = []
    if number < 2:
        return 'Invalid Input'
    for n in range(1,number**2+1):
        y = pdiv(n,number)
        if y == number:
            myans.append(n)
    if len(myans) > 0:
        return myans
    else:
        return True

