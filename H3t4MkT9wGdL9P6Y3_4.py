
def oddish_or_evenish(num):
  return "Evenish" if sum([int(i) for i in str(num)]) % 2 == 0 else "Oddish"

