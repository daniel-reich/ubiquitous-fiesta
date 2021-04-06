
def get_lucky_number(size, nth):
  lst = [i + 1 for i in range(size)]
  isafe = 0
  while lst[isafe + 1] < len(lst):
    filt = lst[isafe + 1]
    lst = [lst[i] for i in range(len(lst)) if i % filt != filt - 1]
    if filt in lst: isafe += 1
  return lst[nth - 1]

