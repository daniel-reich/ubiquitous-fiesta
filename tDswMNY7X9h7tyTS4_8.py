
from math import factorial
def pascals_triangle(n):
    lst = [1]
    for i in range(1, n):
        for j in range(i + 1):
            lst.append(factorial(i)//(factorial(j)*factorial(i-j)))
    return lst

