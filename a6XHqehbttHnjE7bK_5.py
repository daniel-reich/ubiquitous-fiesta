
def is_repdigit(num):
  if num<0: return False
  return len(set(str(num)))==1

