
def count(n):
  n = str(n)
  output = 0
  for i in n:
    if i.isdigit():
      output+= 1
  return output

