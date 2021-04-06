
def covered_integers(lst):
  
  return len(set([ num for e in lst for num in range(e[0] , e[1]+1) ]));

