
def is_good_match(lst):
  temp = []
  if len(lst) % 2 == 1:
    return "bad match"
  for i in range(1,len(lst),2):
    temp.append(lst[i] + lst[i-1])
  return temp

