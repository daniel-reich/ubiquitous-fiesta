
def is_alphabetically_sorted(sentence):
  lst=[]
  sentence=sentence[:-1].lower().split()
  for n in sentence:
    if len(n)>=3 and ''.join(sorted(n))==n:
      lst.append(True)
  if True in lst:
    return True
  else:
    return False

