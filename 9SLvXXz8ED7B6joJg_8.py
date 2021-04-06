
def lets_meet(distance, va, vb):
  a = []
  x = distance / (va + vb)
  y = str(x).split(".")
  a.append(y[0])
  minute = float("0." + y[1])
  minute = minute*60
  minute = str(minute).split(".")
  a.append(minute[0])
  second = float("0." + minute[1])
  second = second*60
  a.append(int(second))
  return "{}h {}min {}s".format(a[0], a[1], a[2])

