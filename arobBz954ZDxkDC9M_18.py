
def next_prime(num):
    if num >1:
        for i in range(2,num):
            while num%i == 0:
                return next_prime(num+1)
                break
        else:
            return num
    else:
        return num

