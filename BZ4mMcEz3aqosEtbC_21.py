
def mean(num):
  sum = 0
  for i in range(len(str(abs(num)))):
    sum += int(str(abs(num))[i])
  return int((sum/len(str(abs(num)))))

