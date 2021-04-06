
def percentage_changed(o, n):
  p = round(abs(int(o[1:]) - int(n[1:]))*100/int(o[1:]))
  return "{0}% {1}".format(p,"decrease" if int(o[1:])>int(n[1:]) else "increase")

