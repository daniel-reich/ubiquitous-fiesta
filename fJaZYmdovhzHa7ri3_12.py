
def max_collatz(num):
  lst = [num]
  while num != 1:
    if num % 2 != 0:
      num = (num * 3) + 1
      lst.append(num)
    else:
      num //= 2
      lst.append(num)
  max_val = max(lst)
  return max_val

