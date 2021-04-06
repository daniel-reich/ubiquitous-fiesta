
def bugger(num):
  def makeList(num):
    a = [int(x) for x in str(num)]
    return a
  def product(lst):
    pro=1
    i=0
    while i<len(lst):
      pro*=lst[i]
      i+=1
    return pro
  prod  = num
  count=0
  while len(str(prod))>1:
    lst = makeList(prod)
    prod  = product(lst)
    count+=1
  return count

