
def first_non_repeated_character(txt):
  if not txt:
    return False
  else:
    if len([i for i in txt if txt.count(i)==1])==0:
      return False;
    else:
      return [i for i in txt if txt.count(i)==1][0]

