
def merge_arrays(a, b):
  new_lst = []
  len_a = len(a)
  len_b = len(b)
  bigger = max(len_a, len_b)
  for index in range(bigger):
    if len_a > index:
      new_lst.append(a[index])
    if len_b > index:
      new_lst.append(b[index])
  return new_lst

