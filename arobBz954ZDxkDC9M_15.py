
def next_prime(num):
  
    prime = []
    for i in range(num, num*2):
        count = 0
        for k in range(1,i+1):
            if not (i % k) : count +=1
        if count == 2:
            prime.append(i)
    return (prime[0])

