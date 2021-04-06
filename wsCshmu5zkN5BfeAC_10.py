
def divisible_by_left(n):
  n = str(n)
  lst = [False]
  for i in range(1,len(n)):
    try:
      lst.append(not bool(int(n[i])%int(n[i-1])))
    except ZeroDivisionError:
      lst.append(False)
  return lst

