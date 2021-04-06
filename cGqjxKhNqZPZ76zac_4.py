
def fire(m, c):
  return 'BOOM' if m['ABCDE'.index(c[0])][int(c[1])-1] == '*' else 'splash'

