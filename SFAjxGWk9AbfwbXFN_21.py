
def primes_below_num(n):
    list=[]
    for i in range(2,n+1):
      if not[j for j in list if not i%j]:
        list.append(i)
    return list

