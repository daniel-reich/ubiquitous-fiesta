
def currently_winning(s):
  return ["Y" if sum(s[:i+1:2]) > sum(s[1:i+2:2]) else "O" if sum(s[:i+1:2]) < sum(s[1:i+2:2]) else "T" for i in range(0,len(s),2)]

