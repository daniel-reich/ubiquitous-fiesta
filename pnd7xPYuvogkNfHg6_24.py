
def get_best_student(g):
​
  s = list( map( lambda x: sum(x), g.values() ) )
  s = zip( list( g.keys() ), s )
  return max( s, key=lambda x:x[1] )[0]

