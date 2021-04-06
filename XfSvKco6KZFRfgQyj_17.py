
def find_a_seat(n, lst):
  r = [x for x in lst if x<=n/len(lst)*.5]
  return lst.index(r[0]) if r else -1

