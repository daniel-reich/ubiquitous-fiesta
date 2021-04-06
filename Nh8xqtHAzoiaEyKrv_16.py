
def correct_sentences(s):
  lst = s.split()
  lst[0] = lst[0].capitalize()
  for i in range(1,len(lst)-1):
    if lst[i].istitle():
      lst[i-1]=lst[i-1]+"."
  if not lst[len(lst)-1].endswith("."):
    lst[len(lst)-1] = lst[len(lst)-1]+'.'
  return ' '.join(lst)

