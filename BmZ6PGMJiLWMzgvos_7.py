
def is_special_array(lst):
  return all(lst[i]%2==i%2 for i in range(len(lst)))

