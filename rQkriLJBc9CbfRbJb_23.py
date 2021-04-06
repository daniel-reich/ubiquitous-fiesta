
def index_of_caps(word):
  caps_list = []
  for i in word:
    if i.isupper():
      caps_list.append(word.index(i))
  return caps_list

