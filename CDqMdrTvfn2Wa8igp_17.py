
def next_element(lst):
  n = len(lst)
  d = lst[1] - lst[0]
  answer = (lst[1] + (n - 1) * d)
  lst.append(answer)
  return answer

