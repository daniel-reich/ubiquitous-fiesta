
f=lambda n:0**n or n*f(n-1)
eval_factorial=lambda l:sum(f(int(s[:-1]))for s in l)

