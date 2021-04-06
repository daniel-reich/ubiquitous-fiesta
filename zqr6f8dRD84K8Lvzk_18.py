
def hex_lattice(n):
  if n == 1:
    return " o "
  for p in range(n):
    if 1 + 3*p*(p+1) == n:
      break
  if p == n-1:
    return "Invalid"
  lines = []
  lmin = p + 1
  lmax = 2*p + 1
  for long in range(lmin,lmax+1):
    lines.append(" "*(lmax-long+1) + "o "*(long-1) + "o" + " "*(lmax-long+1))
  lines.extend(lines[:-1][::-1])
  return "\n".join(lines)
  
​
print(hex_lattice(21))

