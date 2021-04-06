
def sum_primes(lst):
    count1 = 0
    if lst != []:
        for i in lst:
            if i > 1:
                for j in range(2,i):
                    if (i%j)==0:
                        break
                else:
                    count1 += i
            else:
                pass
        return count1
    else:
        return None

