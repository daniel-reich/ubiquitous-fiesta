
ends_add_to_10=lambda n:sum([int(x[0])+int(x[-1])==10for x in map(lambda z:str(z).replace('-',''),n)])

