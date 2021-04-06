
def is_zygodrome(num):
  num=str(num)
  if len(num)==1: return False
  if len(set(num))==1: return True
  if num[0]!=num[1]: return False
  while num[0]==num[1]: num=num[1:]
  return is_zygodrome(num[1:])

