
def loves_me(n):
  output = ""
  s1, s2 = "Loves me", "Loves me not"
  
  for i in range(1, n):
    if i % 2 == 1:
      output += s1 + ', '
    else:
      output += s2 + ', '
  if n % 2 == 1:
    output += s1.upper()
  else:
    output += s2.upper()
  return output

