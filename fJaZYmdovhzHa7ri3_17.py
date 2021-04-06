
def max_collatz(num):
  greatest = num
  current = num
  while True:
    if current == 1:
      return greatest
    else:
      if current % 2 == 0:
        current = current // 2
      else:
        current = current * 3 + 1
      greatest = max(greatest,current)

