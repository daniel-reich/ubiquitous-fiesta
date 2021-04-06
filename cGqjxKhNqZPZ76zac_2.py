
def fire(mtx, cdn):
  l = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
  n = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}
  x = mtx[l[cdn[0]]][n[cdn[-1]]]
  return "BOOM" if x == "*" else "splash"

