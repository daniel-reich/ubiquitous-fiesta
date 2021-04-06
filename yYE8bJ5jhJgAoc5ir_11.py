
def bugger(num):
  if len(str(num)) == 1:
    return 0
  count = 0
  while len(str(num)) > 1:
    num_str = list(str(num))
    for i in range(0, len(num_str) - 1):
      num_str[i] = num_str[i] + '*'
    num = eval(''.join(num_str))
    count = count + 1
  print(num)
  return(count)

