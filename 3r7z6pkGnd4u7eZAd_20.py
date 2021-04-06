
def mark_maths(lst):
  correct = 0
  for l in lst:
    ls = l.split("=")
    ls1 = eval(ls[0])
    answer = int(ls[1])
    if ls1 == answer:
      correct += 1
  percent = round((correct / len(lst)) * 100, 0)
  p = str(percent)
  if p[len(p) - 1] == "0":
    p = p[0:len(p) - 2]
  return str(p) + "%"

