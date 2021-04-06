
def wiggle_string(s): #w/o built-in
  def l(st):
    count = 0
    while st != "":
      count += 1
      st = st[1:]
    return count
  w, c = [s], s[::-1]
  while l(w[-1]) < 2* l(s):
    c += " "
    w += [c]
  w_s = [s] + [x[::-1] for x in w][1:]
  return w_s + w_s[::-1][1:]

