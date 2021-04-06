
def countdown(n, txt):
  r=""
  while n>0:
    r +=str(n)+". "
    n -=1
  return r+txt.upper()+"!"

