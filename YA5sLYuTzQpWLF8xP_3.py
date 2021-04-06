
def clean_up_list(lst):
  even = [i for i in map(int, lst) if i%2 == 0]
  odd = [i for i in map(int, lst) if i%2 == 1]
  return [even, odd]

