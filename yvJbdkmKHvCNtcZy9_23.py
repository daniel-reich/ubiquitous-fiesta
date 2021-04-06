
def is_disarium(n):
  answer = 0
  for i,j in enumerate(str(n)):
    answer += int(j)**int(i+1)
  return answer == n

