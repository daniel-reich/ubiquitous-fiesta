
def sort_word(word):
  lst = [w for w in word]
  wword =""
  for i in sorted(lst):
    if i.isupper():
      wword += i
    else:
      wword += i
  return wword

