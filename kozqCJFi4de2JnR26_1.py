
fib_str=lambda n,f:', '.join(f)if n==2 else fib_str(n-1,f+[f[-1]+f[-2]])

