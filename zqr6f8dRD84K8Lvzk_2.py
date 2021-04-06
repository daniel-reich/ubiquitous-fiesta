
def hex_lattice(n):
  for l in range(1, n//6+2):
    if 3*l*(l-1) == n-1:
      hex = ""
      for i in list(range(l)) + list(range(l-2, -1, -1)):
        hex += ' '*(l-i) + 'o '*(l+i) + ' '*(l-i-1) + '\n'
      return hex.strip('\n')
  return "Invalid"

