
def is_triplet(n1, n2, n3):
  list = [n1, n2, n3]
  sorted_list = sorted(list)
  if sorted_list[0]**2 + sorted_list[1]**2 == sorted_list[2]**2:
    return True
  else:
    return False

