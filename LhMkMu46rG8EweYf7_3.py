
def sort_by_letter(lst):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  sorted_lst = []
  for l in letters:
    for i in lst:
      if l in i:
        lst.remove(i)
        sorted_lst.append(i)
  return sorted_lst

