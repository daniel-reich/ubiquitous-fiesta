
def fibonacci(num):
  c = [0, 1]
  while len(c) < num +2:
    next_num = c[-1] + c[-2]
    c.append(next_num)
  return c[-1]

