
def prime_numbers(x):
    primearray=[]
    for i in range(1, x):
        if checkprime(i) == True:
            primearray.append(i)
        else:
            continue
    return(len(primearray))
        
def checkprime(x):
    if x >= 2:
        for y in range(2, x):
            if not(x%y):
                return False
    else:
        return False
    return True

