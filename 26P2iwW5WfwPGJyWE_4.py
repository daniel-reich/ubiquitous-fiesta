
possibly_perfect=lambda k,a:all(x!=y for x,y in zip(k,a))or all(x==y or x=='_'for x,y in zip(k,a))

