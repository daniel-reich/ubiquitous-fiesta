
import operator
def most_frequent_char(lst):
  adict = {}
  for i in range(len(lst)):
    for item in lst[i]:
      if item not in adict:
        adict[item] = 1
      else:
        adict[item] += 1
  a = max(adict.items(), key=operator.itemgetter(1))[1]
  result = []
  for k,v in adict.items():
    if v == a:
      result.append(k)
  return sorted(result)

