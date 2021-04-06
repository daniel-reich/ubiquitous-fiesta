
def find_longest(s, mword=""):
  if len(s) == 0:
    if '\'' in mword: 
      mword = mword.split('\'')[0].lower()
    return "".join([c for c in mword if c.isalpha()]).lower()
​
  if len(s.split()[0]) > len(mword):
    mword = s.split()[0]
  
  return find_longest(" ".join(s.split()[1:]), mword)

