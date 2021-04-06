
num_split=lambda n:[int(x)*10**i*(1,-1)[n<0]for i,x in enumerate(str(n)[::-1].strip('-'))][::-1]

