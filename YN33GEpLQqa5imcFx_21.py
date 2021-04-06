
def pascals_triangle(row):
    k = row + 1
    def fact(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    return ' '.join(str(fact(row) // (fact(n) * fact(row - n))) for n in range(k))

