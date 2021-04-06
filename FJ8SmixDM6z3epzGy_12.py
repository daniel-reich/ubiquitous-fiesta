
def check_perfect(num):
  lst = []
  for i in range(num-1, 0, -1):
    if num%i == 0:
      lst.append(i)
  return sum(lst) == num

