
def show_the_love(lst):
  smallest  = min(lst)
  to_add_to_smallest  =  sum([e/4 for e in lst if e != smallest])
  return [e -e/4 if e != smallest else e + to_add_to_smallest for e in lst];

