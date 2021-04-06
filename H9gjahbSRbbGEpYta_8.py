
def multiply(n1, n2):
  pos = n1 > 0 and n2 > 0 or n1 < 0 and n2 < 0
  n1, n2 = abs(n1), abs(n2)
  count = 1
  answer = n1
  while count < n2:
    answer += n1
    count += 1
  if pos == False:
    return -answer
  return answer

