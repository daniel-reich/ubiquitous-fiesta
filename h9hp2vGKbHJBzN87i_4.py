
def partially_hide(phrase):
  lst = []
  for n in phrase.split(' '): 
    lst.append(n[0] + '-'*(len(n)-2) + n[-1]) 
  return ' '.join(lst)

