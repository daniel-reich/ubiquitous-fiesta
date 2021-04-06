
def left_side(lst):
  final = [0]
  for i in lst[1:]:
    count = 0
    for j in lst[:lst.index(i)]:
      if i>j:
        count+=1
    final.append(count)
  return final
​
def right_side(lst):
  final = [0]
  for i in lst[:-1][::-1]:
    count = 0
    for j in lst[lst.index(i):]:
      if i>j:
        count+=1
    final.append(count)
  return final[::-1]

