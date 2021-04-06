
number_of_swaps=lambda l:sum(a>b for i,a in enumerate(l)for b in l[i:])

