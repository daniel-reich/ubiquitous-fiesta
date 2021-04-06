
def how_mega_is_it(n):
  if abs(n) > 100:
    x = str(abs(n)).split('.')[0]
    y = ["MEGA"]*(len(x)-2) + ["milestone"]
    return ' '.join(y)
  else:
    return "not a mega milestone"

