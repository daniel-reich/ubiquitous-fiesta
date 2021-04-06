
def is_pandigital(n):
  holder = []
  for num in str(n):
    holder.append(num)
​
  unique = list(map(int, list(dict.fromkeys(holder))))
  values_to_check = list(range(0, 10))
​
  result = all(elem in unique for elem in values_to_check)
  return(result)

