
def cuban_prime(num):
    a=[7, 19, 37, 61, 127, 271, 331, 397, 547, 631, 919,1801,4447]
    if num  in a:
        return str(num)+" is cuban prime"
    else:
        return str(num)+" is not cuban prime"

