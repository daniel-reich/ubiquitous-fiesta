
def prime(integer):
    for number in range(2,(integer//2)+1):
        if integer%number == 0:
            return False
    if integer <= 1:
        return False
    return True
​
def prime_numbers(ranger):
    counter = 0
    for i in range(ranger):
        if prime(i):
            counter += 1
            
    return counter

