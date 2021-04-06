
def reverse(txt):
  lst = txt.split(' ')
  lst_reversed = []
  for word in lst:
    if len(word) >= 5 :
      lst_reversed.append(word[::-1])
    else:
      lst_reversed.append(word)
    
  return ' '.join(lst_reversed)

