
def is_special_array(lst):
  return all(map(lambda x: x % 2 == 0, lst[0::2])) and all(map(lambda x: x % 2,lst[1::2]))

