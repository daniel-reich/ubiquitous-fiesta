
def prime_divisors(num):
    count=0
    lst=[]
    for i in range(2,num+1):
        if num %i ==0:
            for j in range(2,i):
                if i % j == 0:
                    count+=1
            if count == 0:
                lst.append(i)
        count=0
    return lst

