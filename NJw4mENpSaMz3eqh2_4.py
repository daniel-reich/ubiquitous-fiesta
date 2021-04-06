
def is_undulating(num):
  num  =  str(num);
  return len(num) >= 3  and ( (num[:2]*len(num))[:len(num)] == num)

