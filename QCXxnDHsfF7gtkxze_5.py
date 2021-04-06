
def mystery_func(num):
  txt = str(num)
  result = 1
  for i in range(len(txt)):
    result *= int(txt[i])
  return result

