
def index_of_caps(word):
  id = 0
  id_lst = []
  print(word)
  for c in word:
    if ord(c) >= 65 and ord(c) <= 90:
      id_lst.append(id)
    id += 1
  return(id_lst)

