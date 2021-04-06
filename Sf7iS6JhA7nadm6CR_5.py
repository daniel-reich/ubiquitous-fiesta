
import math
​
def digits(num):
    n =[]
    while(num > 0):
        n.append(num%10)
        num=math.floor(num/10)
    return n
​
def divisibility_rule(n):
    seq = [1, 10, 9, 12, 3, 4]
    before = 0
    current =n
    while(current!=before):
        i=1
        num = digits(n)
        n=0
        for j in range (len(num)):
            n+=num[j]*seq[i%6-1]
            i+=1
        before = current
        current = n
    return n

