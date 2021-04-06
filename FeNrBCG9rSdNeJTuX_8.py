
import time
def max_possible(n1, n2):
  startTime = time.time()
  n1 = list(map(int,str(n1)))
  n2 = list(map(int,str(n2)))
  n2.sort(reverse=True)
  for j in range(len(n2)):
    for i in range(len(n1)):
      if n2[j] > n1[i]:
        n1[i] = n2[j]
        break
  num = int("".join(str(e) for e in n1))
  endTime = time.time()
  print("Time : ",endTime-startTime)
  return num

