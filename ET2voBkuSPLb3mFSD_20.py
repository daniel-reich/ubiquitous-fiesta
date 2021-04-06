
def sum_every_nth(numbers, n):
    return sum(numbers[x] for x in range(n - 1, len(numbers), n))

