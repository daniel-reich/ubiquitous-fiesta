
def arithmetic_progression(start, diff, n):
  
  list = []
  while len(list) < n:
    list.append(str(start))
    start += diff
  answer = ", ".join(list)
  return answer

