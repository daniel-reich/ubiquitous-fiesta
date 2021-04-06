
def break_point(num):
  num = str(num)
  lst = [[[int(x) for x in num[i:]],[int(x) for x in num[:i]]] for i in range(1,len(num))]
  return max([sum(x[0])==sum(x[1]) for x in lst])

