
def possible_path(lst):
  good_values = set(frozenset(k) for k in ['12', '2H', '4H', '43'])
  input_values = set(frozenset(str(i)+str(j)) for i, j in zip(lst, lst[1:]))
  
  return input_values.issubset(good_values)

