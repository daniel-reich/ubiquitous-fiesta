
def simple_pair(lst, n):
  length = len(lst)
  for index in range(length):
    if lst[index] != 0 and n % lst[index] == 0:
      quo = n//lst[index]
      if quo in lst[:index] or quo in lst[index+1:]:
        return [lst[index],quo]
  return None

