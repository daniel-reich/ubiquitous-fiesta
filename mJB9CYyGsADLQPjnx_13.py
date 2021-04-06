
def first_non_repeated_character(l):
    
  try:return sorted([s for s in set(l) if l.count(s)==1],key=l.index)[0]
  except:return 0

