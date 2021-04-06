
def staircase(n):
  string = ""
  if n < 0:
    for i in range(0,abs(n)):
      string += "_" * i + "#" * (abs(n)-i) + "\n"
  else:
    for i in range(1,n+1):
      string += "_" * (n-i) + "#" * i + "\n"
  return string[:len(string)-1]

