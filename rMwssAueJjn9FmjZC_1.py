
number_pairs=lambda t:(lambda l:sum(l.count(x)//2for x in set(l)))(t.split()[1:])

