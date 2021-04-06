
def order(lst):
   z = sorted([(x,i) for i, x in enumerate(lst)])
   return [i for x,i in z]

