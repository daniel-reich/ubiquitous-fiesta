
def move(word):
  import string
  alph = [i for i in string.ascii_lowercase]
  lst = []
  for letter in word:
    nxt_i = alph.index(letter)+1
    lst.append(alph[nxt_i])
  return "".join(lst)

