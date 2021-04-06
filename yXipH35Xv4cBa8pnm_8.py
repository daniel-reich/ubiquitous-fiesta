
def microwave_buttons(time):
  a, b = [int(x) for x in time.split(":")]
  a = (a * 60 + b) // 30
  return min((a if a else 10000, button(time))) + 1
​
def button(x):
  x=x.replace(":", "")
  for y in range(len(x)):
    if int(x[y]) > 0:
      return len(x[y:])
  return 0

