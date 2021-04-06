
def next_number(num):
  n = num
  num = list(str(num))
  if sorted(num)[::-1] == num:
    return n
  for i in range(2, len(num) + 1):
    temp = sorted(num[-i:])
    start = ''.join(num[:-i])
    for x in range(len(temp)):
      check = int(start + ''.join([temp[x]] + temp[:x] + temp[x + 1:]))
      if check > n:
        return check

