
def get_lucky_number(size, nth):
  lst = list(range(1,size+1))
  used = [1]
  step = 2
  while len(lst) > step:
    lst = [lst[i] for i in range(len(lst)) if (i+1)%step != 0]
    used.append(step)
    step = [i for i in lst if i not in used][0]
  return lst[nth-1]

