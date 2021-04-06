
def sum_primes(list_1):
    total = 0
    if list_1 == []:
        return None
    
    if 1 in list_1:
        total -= 1
    #find primes
​
    for i in range(0, len(list_1)):
        #print(list_1[i])
        counter = 0
        for j in range(2, list_1[i]):
​
            if list_1[i] % j == 0:
                #print("NOT PRIME", list_1[i])
                counter += 1
​
        if counter == 0:
            #print("PRIME", list_1[i])
            total+= list_1[i]
​
    #print("total", total)
    return total

