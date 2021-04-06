
def is_subset(lst1, lst2):
  answer =[]
  for num in lst1:
    if num in lst2:
      answer.append(num)
  return answer == lst1

