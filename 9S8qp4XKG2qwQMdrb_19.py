
def ways_to_climb(n):
    if n <= 1:
        return 1
    ways = {step: 0 for step in range(n + 1)}
    ways[0] = 1
    for step in range(n - 1):
        ways[step+1] += ways[step]
        ways[step+2] += ways[step]
    ways[n] += ways[n-1]
    return ways[n]

