
def sort_by_letter(lst):
  for i in range(len(lst)) :
    for j in range(len(lst[i])) :
      if lst[i][j].isalpha() :
        lst[i] = lst[i][j] + lst[i]
        break
  lst = sorted(lst)
  return [i[1:] for i in lst]

