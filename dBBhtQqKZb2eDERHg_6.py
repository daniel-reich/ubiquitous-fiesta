
def numberSequence(n):
  if n <= 0:
    return "-1"
  elif n == 1:
    return "1"
  elif n % 2 == 1:
    k = str(int(numberSequence(n-1)[0])+1) + " " + numberSequence(n-1)[:numberSequence(n-1).index("1")]
    return k + "1" + k[::-1]
  else:
    k = numberSequence(n-1)[:numberSequence(n-1).index("1")+1]
    return k + " " + k[::-1]

