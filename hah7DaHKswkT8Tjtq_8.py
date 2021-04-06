
def separate_numbers(s):
  A=[int(s[:i]) for i in range(1, len(s)//2+1) if int(s[:i])]
  for x in A:
    if s in ''.join([str(x+i) for i in range(10)]):
      return "YES {}".format(x)
  return 'NO'

