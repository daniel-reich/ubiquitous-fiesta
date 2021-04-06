
def fire(m, c):
  return ['splash','BOOM'][m[ord(c[0])-65][int(c[1])-1] == '*']

