
def chocolates_parcel(n_small, n_big, order):
   solutions={x for x in range(n_small+1) for y in range(n_big+1) if 2*x+5*y==order}
   return -1 if len(solutions)==0 else  sorted(solutions)[0]

