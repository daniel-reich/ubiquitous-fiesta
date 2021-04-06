
def func(num):
  txt = str(num)
  return sum(int(i) - len(txt) for i in txt)

