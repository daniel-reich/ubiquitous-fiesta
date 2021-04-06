
def repeated(s):
  return any([len(s)==len(s[:i])*s.count(s[:i]) for i in range(2,len(s))]) if len(s)>1 else False

