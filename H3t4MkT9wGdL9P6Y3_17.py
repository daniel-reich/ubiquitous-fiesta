
def oddish_or_evenish(num):
  if sum(map(int, str(num))) % 2 == 0 : return "Evenish"
  return "Oddish"

