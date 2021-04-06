
def break_point(num):
  num = [int(i) for i in str(num)]
  if len(num) == 2:
    return True if num[0] == num[1] else False 
  else:
    return any([sum(num[:i]) == sum(num[i:]) for i in range(len(num))])

