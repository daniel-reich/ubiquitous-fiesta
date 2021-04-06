
def max_ham(s1, s2):
  if len([x for x in s1 if x in s2]) == (len(s1) & len(s2)):
    ham_dis = len([x for x in [[a, b] for a, b in zip(s1, s2)] if x[0] != x[1]])
    if ham_dis == len(s1):
      return True
    else:
      return ham_dis
  return False

