
def first_before_second(s, first, second):
  fInd = max([i for i in range(len(s)) if s[i] == first])
  sInd = min([i for i in range(len(s)) if s[i] == second])
  return fInd < sInd

