
def repeated(s):
  return True in [s[:i]*(len(s)//i)==s for i in range(1,len(s))]

