
def covered_integers(lst):
​
  s = [x for i in range(len(lst)) for x in list(range(lst[i][0], lst[i][1]+1)) ]
​
  return(len(set(s)))

