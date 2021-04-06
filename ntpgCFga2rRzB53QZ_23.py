
def staircase(n):
  output = ""
  if(n > 0):
    for i in range(n):
      output += ("_" * (n - i - 1)) + ("#" * (i + 1))
      if(i < n - 1):
        output += "\n"
  else:
    for i in range(n * -1):
      output += ("_" * (i)) + ("#" * (-n - i))
      if(i < -n - 1):
        output += "\n"
  return output

