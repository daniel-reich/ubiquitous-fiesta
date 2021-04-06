
digits_count = lambda n: 1 if abs(n) < 10 else 1 + digits_count(n//10)

