
def award_prizes(names):
  prize  = ["Gold", "Silver", "Bronze", "Participation"]
  t = sorted(list(names.items()), key=lambda x: x[1], reverse=True)
  dic = {}
  i = 0
  for x,y in t:
    if i < 3:
      dic.update({x:prize[i]})
      i += 1
    else:
      dic.update({x:prize[i]})
​
  return dic

