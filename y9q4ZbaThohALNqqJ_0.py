
squares = set(i * i for i in range(46342))
def squares_sum(n):
    return any(n - i * i in squares for i in range(int(pow(n, 0.5)) + 1))

