
def oddish_or_evenish(num):
  return "Evenish" if not sum(int(i) for i in str(num)) % 2 else "Oddish"

