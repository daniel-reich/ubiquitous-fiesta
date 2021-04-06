
def largest_even(lst):
  answer = []
  for n in lst:
    if n % 2 == 0:
      answer.append(n)
  if len(answer) == 0:
    return -1
  return answer[-1]

