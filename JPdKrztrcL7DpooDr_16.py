
def collatz(n):
  list_nums = []
  list_nums.append(n)
  while n != 1:
    if n % 2 == 0:
      n = n / 2
      list_nums.append(n)
    else:
      n = (n * 3) + 1
      list_nums.append(n)
      
  return [len(list_nums) - 1, max(list_nums)]

