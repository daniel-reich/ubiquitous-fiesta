
def divide(lst, n):
  sublst = []
  answer = []
  for item in lst:
    if n >= sum(sublst) + item: sublst.append(item)
    else:
      answer.append(sublst)
      sublst = [item]
  answer.append(sublst)
  return answer

