
def find_the_difference(s, t):
  for eachletter in t:
    if eachletter not in s:
      return eachletter
    elif t.count(eachletter) > s.count(eachletter):
      return eachletter

