
def primorial(n):
​
    def prime(num):
        for i in range(2,int(num/2)+1):
            if num%i == 0:
                return False
        return True
​
​
    output = 1
    i = 2
    count = 0
    while count<n:
        if prime(i):
            output = output * i
            count += 1
            print(i, prime(i))
        i+=1
    return output

