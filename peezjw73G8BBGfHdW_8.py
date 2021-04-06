
def arithmetic_operation(n):
  f,o,l=n.split()
  if o in ["+","-"]:
    if o=="-":
      l="-"+l
    return sum(map(int,[f,l]))
  if o=="*":
    return int(f)*int(l)
  if l=="0":
    return -1
  return int(f)//int(l)

