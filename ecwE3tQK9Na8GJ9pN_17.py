
def little_big(n):
  if n == 1:
    return 5
  if n == 2:
    return 100
  current_position = 2
  little_num = 5
  big_num = 100
  for i in range(2, n + 1):
    little_num += 1
    current_position += 1
    if current_position == n:
      return little_num
    big_num *= 2
    current_position += 1
    if current_position == n:
      return big_num

