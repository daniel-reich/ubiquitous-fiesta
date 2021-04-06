
def same_line(lst):
  def incl(a, b):
    if (a[0]-b[0]) == 0: return float("inf")
    return (a[1]-b[1]) / (a[0]-b[0])
  return incl(*lst[:2]) == incl(*lst[1:])

