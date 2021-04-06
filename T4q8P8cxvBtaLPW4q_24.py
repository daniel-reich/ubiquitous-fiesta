
def extract_primes(num):
    num_str = str(num)
    a = []
    for i in range(len(num_str)):
        for j in range(len(num_str)-i):
            if num_str[j] != '0':
                #print(num_str[j:j+i+1])
                a.append(check_prime(num_str[j:j+i+1]))
    return sorted(list(filter(lambda b : b != 1, a)))
​
def check_prime(num):    
    if int(num) == 1: return 1
    elif int(num) == 0: return 1
    else:
        for n in range(2,int(int(num)**0.5)+1):
            if int(num) % n == 0: return 1
        return int(num)

