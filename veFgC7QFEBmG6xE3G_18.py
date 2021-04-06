
def is_smooth(sentence):
  l = sentence.split()
  
  for x in range(1, len(l)-1):
    if l[x][0].lower() != l[x-1][-1].lower(): return False
  return True

