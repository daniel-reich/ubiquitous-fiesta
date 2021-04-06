
def true_equations(lst):
  true_list = []
  for i in lst:
    answer=int(i.split('=')[1])
    question = i.split('=')[0]
    if eval(question) == answer:
      true_list.append(i)
  return true_list

