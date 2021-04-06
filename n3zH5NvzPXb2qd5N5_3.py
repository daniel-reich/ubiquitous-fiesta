
def how_mega_is_it(n):
  if len(str(n))<=2:
    return "not a mega milestone"
  else:
    x  = len(str(abs(int(n))))-2
    me = " ".join(["MEGA" for x in range(x)])
    return "{Mega} milestone".format(Mega = me)

