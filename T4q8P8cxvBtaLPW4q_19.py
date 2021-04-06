
import math
def is_prime(n):
    i=2
    while(i<=math.sqrt(n)):
        if n%i ==0 and n!=i:
            return False
            break
        i+=1
    return True
​
def extract_primes(num):
    str1=str(num)
    lst=[]
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            str2=str1[i:j+1]
            if str2[:1] == '0' or str2[-1] =='0':
                str2=1
            if is_prime(int(str2)) and int(str2)!=1 and int(str2)!=0:
                lst.append(int(str2))
    lst.sort()
    return lst

