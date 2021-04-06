
def leader(arr):
  arr2 = []
  arr2 += arr
  arr.sort()
  index = arr2.index(arr[-1])
  answer = arr2[index:]
  for i in range(len(answer)-1):
    if answer[i] < answer[i+1]:
      answer.pop(i)
  
  return answer

