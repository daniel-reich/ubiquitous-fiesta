
def digits_count(num,i=1):
  if abs(num)//(10**i)==0:return i
  return digits_count(num,i+1)

