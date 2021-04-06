
def reverse_odd(txt):
  a = txt.split()
  temp = []
  for i in a:
    if len(i)%2 == 0:
      temp.append(i)
    else:
      temp.append(i[::-1])
  
  return " ".join(temp)

