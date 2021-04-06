
def strong_password(pwd):
  ns = '0123456789'
  ls = 'abcdefghijklmnopqrstuvwxyz'
  us = ls.upper()
  ss = '!@#$%^&*()-+'
  nx = not any(c in ns for c in pwd)
  lx = not any(c in ls for c in pwd)
  ux = not any(c in us for c in pwd)
  sx = not any(c in ss for c in pwd)
  return max(6-len(pwd), nx+lx+ux+sx)

