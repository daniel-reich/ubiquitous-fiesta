
def is_prime(list_of_primes, number):
    first = 0
    last = len(list_of_primes)-1
    found = False
    while first <= last and not found:
        middle = (first + last)//2
        if list_of_primes[middle] == number:
            found = True
        else:
            if number < list_of_primes[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return "yes" if found else "no"

