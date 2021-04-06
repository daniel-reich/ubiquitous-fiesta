
def sum_of_evens(matrix):
    total = 0
    for lst in matrix:
        for number in lst:
            if number % 2 == 0:
                total += number
​
    return total

