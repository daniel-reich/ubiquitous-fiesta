
def get_level(lst):
  l = [lst[i] - lst[i-1] for i in range(1,len(lst))]
  return 1 + get_level(l) if sum(l) != 0 else 0
​
def seq_level(lst):
  d = ["Linear","Quadratic","Cubic"]
  return d[get_level(lst)-1]

