
ways_to_climb = f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)

