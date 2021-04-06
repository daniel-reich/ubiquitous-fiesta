
def little_big(n):
    result = [5, 100]
    for i in range(2, n//2 + 2):
        result.extend([i+4, 2**(i - 1) * 100])
    return result[n-1]

