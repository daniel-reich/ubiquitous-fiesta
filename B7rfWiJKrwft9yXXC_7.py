
def sort_descending(num):
  new_lst = [number for number in str(num)]
  new_lst.sort(reverse = True)
  return int("".join(new_lst))

