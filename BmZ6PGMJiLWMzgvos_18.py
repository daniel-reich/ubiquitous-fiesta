
def is_special_array(lst):
  return all([i % 2 == 0 and lst[i] % 2 == 0 or  i % 2 == 1 and lst[i] % 2 == 1 for i in range(len(lst))])

