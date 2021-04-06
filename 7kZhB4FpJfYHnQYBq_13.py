
import math
def lcm_three(num):
    newlist = []
    total = 1
    num1 = prime_factorization(num[0])
    num2 = prime_factorization(num[1])
    num3 = prime_factorization(num[2])
    totalset = list(set(num1 + num2 + num3))
    for eachnum in totalset:
        if eachnum in num1:
            if eachnum in num2:
                if eachnum in num3:# if number is in all three
                    for i in range(max(num1.count(eachnum),num2.count(eachnum),num3.count(eachnum))):
                        newlist.append(eachnum)
                else:
                    # if number is in two
                    for i in range(max(num1.count(eachnum),num2.count(eachnum))):
                        newlist.append(eachnum)
            else:
                # if number is in one
                for i in range(num1.count(eachnum)):
                    newlist.append(eachnum)
        #if number is not in num1
        elif eachnum in num2:
            if eachnum in num3:
                for i in range(max(num2.count(eachnum),num3.count(eachnum))):
                    newlist.append(eachnum)
            else:
                for i in range(num2.count(eachnum)):
                    newlist.append(eachnum)
        else:
            for i in range(num3.count(eachnum)):
                newlist.append(eachnum)
    for eachnumber in newlist:
        total = total * eachnumber
    return total
    
def prime_factorization(num):
    if is_prime(num):
        return [num]
    newlist = []
    for i in range(2,num):
        if is_prime(i) and num % i == 0:
            while(num % i == 0):
                num = num / i
                newlist.append(i)
    newlist.append(num)
    return newlist
    
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

