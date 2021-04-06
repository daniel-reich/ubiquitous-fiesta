
def func_sort(lst):
  def call_depth(f):
    d = 0;
    while callable(f):
      d +=1
      f = f()
    return d
  
  return(sorted(lst, key=call_depth))

