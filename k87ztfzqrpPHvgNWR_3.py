
def widen_streets(lst, n):
  result=[]
  for x in range(len(lst)):
    sub=lst[x].split(" ")
    if('' in sub):
      sub.remove('')
      sub.insert(sub.index(''),'-')
      sub.remove('')
    print(sub)
    substring=""
    for x in sub:
      substring+=x+(n*" ")
    result.append(substring[0:len(substring)-n].replace("-", " "))
  return result

