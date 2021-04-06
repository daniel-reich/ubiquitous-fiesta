
i_sqrt = lambda n: "invalid" if n < 0 else 0 if n < 2 else 1 + i_sqrt(n**0.5)

