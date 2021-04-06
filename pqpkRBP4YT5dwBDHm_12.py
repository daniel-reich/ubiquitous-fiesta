
def show_the_love(lst):
  return [n * 0.75 + (sum(lst) / 4) * (n == min(lst)) for n in lst]

