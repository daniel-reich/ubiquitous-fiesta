
def mystery_func(num):
  s, mult = "", 1
  while mult < num:
    mult *= 2
    s += "2"
  return int(s[1:]+str(num-mult//2))

