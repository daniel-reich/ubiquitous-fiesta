
f=lambda x:', '.join(x+[x[-1]+x[-2]])
fibo_word=lambda n:n<2and'invalid'or n==2and'b, a'or f(fibo_word(n-1).split(', '))

