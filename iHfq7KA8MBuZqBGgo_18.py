
def is_legitimate(lst):
  def all_zeroes(l):
    for i in l:
      if i != 0:
        return False
    return True
  rotated_lst = list(zip(*lst))
  return all_zeroes(lst[0]) and all_zeroes(lst[-1]) and all_zeroes(rotated_lst[0]) and all_zeroes(rotated_lst[-1])

