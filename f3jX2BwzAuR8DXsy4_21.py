
def fact_of_fact(n):
    result = 1
    for i in range(n):
        result *= (i + 1) ** (n - i)
    return result

