
def happy(n):
    total = 0
    count = 0
    n = [int(x) for x in str(n)]
    
    while True:
        for numbers in n:
            total += pow(numbers, 2)
        count += 1
        
        if total > 1:
            n = [int(x) for x in str(total)]
            total = 0
        else:
            return True
        if count == 10:
            return False

