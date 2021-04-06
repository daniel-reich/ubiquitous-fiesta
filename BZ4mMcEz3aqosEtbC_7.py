
def mean(num):
  count = 0
  str_num = str(num)
  for i in range(len(str_num)):
    count += int(str_num[i])
  return int(count/len(str_num))

