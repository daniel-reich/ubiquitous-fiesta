
def sum_every_nth(numbers, n):
    suma = 0
    i = n
    while i <= len(numbers) :
        suma += numbers[i-1]
        i +=n
    return suma

