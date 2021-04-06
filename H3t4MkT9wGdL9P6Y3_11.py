
def oddish_or_evenish(num):
  num = str(num)
  soma = 0
  for i in num:
    soma += int(i)
  if not soma % 2:
    return "Evenish"
  else:
    return "Oddish"

