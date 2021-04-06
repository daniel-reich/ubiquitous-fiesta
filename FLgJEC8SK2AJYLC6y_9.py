
def possible_path(lst):
  return all(j in POSSIBLE[i] for i, j in zip(lst, lst[1:]))
​
POSSIBLE = {
  1: (2,),
  2: ('H', 1),
  'H': (2, 4),
  4: ('H', 3),
  3: (4,),
}

