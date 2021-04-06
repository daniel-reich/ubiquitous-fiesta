
combinations = c = lambda k, n: n * c(k - 1, n - 1) / k if k else 1

