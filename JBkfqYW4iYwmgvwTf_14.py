
def is_prime(num):
    factor_list = []
    for factors in range(1 , num + 1):
        # print(num , factors)
        if(num % factors == 0):
            # print(num, "is divisible by" , factors)
            factor_list.append(factors)
    #if there are only two elements in the factor list
    if(len(factor_list) == 2):
        return True
    else:
        return False

