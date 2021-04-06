
def ways_to_climb(n):
    s = {1, 2}
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in s if i - x > 0)
        cache[i] += 1 if i in s else 0
    return cache[-1]

