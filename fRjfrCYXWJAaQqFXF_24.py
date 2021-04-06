
def primorial(n):
    primo = 2
    num = 3
    num_of_times = 0
    while True:
        if num_of_times == n-1:
            return primo
        z = 1
        for i in range(num - 3):
            if num % (i+2) == 0:
                z = 0
                break
        if z == 1:
            primo *= num
            num_of_times += 1
        num += 1

