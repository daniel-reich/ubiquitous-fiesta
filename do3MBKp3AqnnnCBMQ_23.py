
import random
​
def numbers():
    A = ['1', '2', '3', '4', '5']
    random.shuffle(A)
    return int(''.join(A))

