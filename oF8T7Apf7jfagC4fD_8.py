
def antipodes_average(lst):
  answer = []
  if len(lst)%2!= 0:
    divide = int(len(lst)/2)
    del(lst[divide])
  first_part = []
  for i in range(len(lst)//2):
    first_part.append(lst[i])
  second_part = []
  for j in range(len(lst)//2,len(lst)):
    second_part.append(lst[j])
  second_part.reverse()
  for x, y in zip(first_part,second_part):
    add = (x+y)/2
    answer.append(add)
  return answer

