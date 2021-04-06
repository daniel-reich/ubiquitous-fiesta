
def partially_hide(phrase):
  lst=phrase.split()
  str=""
  for x in lst:
    m=len(x)-2
    x=x[0]+m*"-"+x[-1]
    str+=" "+x
  return str.strip()

