
def separate_numbers(s):
  ans = []
  for ind in range(1,len(s)//2+1):
    start,test = s[:ind],s[:]
    while test.startswith(start):
      start,test = str(int(start)+1),test[len(start):]
    if test == "": ans += [s[:ind]]
  return "YES "+str(ans[0]) if ans else "NO"

