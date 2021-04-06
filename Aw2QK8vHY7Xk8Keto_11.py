
def longest_word(s):
  print(s)
  lst = s.split(' ')
  lst1 = [len(i) for i in lst]
  x = lst1.index(max(lst1))
  return lst[x]

