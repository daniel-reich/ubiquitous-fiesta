
def expanded_form(num):
  s=list(enumerate(str(num)[::-1]))[::-1]
  l= [int(x[1])*10**x[0] for x in s if int(x[1])!=0]
  l1 = [str(x) for x in l]
  return " + ".join(l1)

