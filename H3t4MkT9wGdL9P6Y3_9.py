
def oddish_or_evenish(num):
  return "Evenish" if sum([int(x) for x in str(num)])%2==0 else "Oddish"

