
def move(word):
  list1 = list(word)
  for i in range(len(list1)):
    list1[i]=chr(ord(list1[i])+1)
  string=''.join(list1)
  return string

