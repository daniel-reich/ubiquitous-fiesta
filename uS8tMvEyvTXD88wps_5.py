
def reverse(txt):
  lst = txt.split(' ')
  for i, word in enumerate(lst[:]):
    if len(word) >= 5:
      lst[i] = lst[i][::-1]
  return ' '.join(lst)

