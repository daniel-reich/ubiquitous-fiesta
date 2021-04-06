
def sum_first_n_nums(lst, n):
 return 0 if n==0 else sum(lst) if n>= len(lst) else sum([x for x in lst if lst.index(x)<n])

