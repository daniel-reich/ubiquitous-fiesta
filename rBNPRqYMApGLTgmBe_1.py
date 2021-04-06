
combinations = lambda k, n: n * combinations(k-1, n-1) / k if k else 1

