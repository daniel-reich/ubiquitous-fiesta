
def longest_substring(digits):
​
  digits = str(digits)
  container = []
  word = ""
​
  for i in range(0, len(digits)):
​
    if len(word) == 0:
​
      word = word + digits[i]
​
    else:
​
      x = int(digits[i])
      y = int(word[-1])
​
      if x % 2 == 0 and y % 2 != 0 or x % 2 != 0 and y % 2 == 0:
        word = word + digits[i]
      else:
        container.append(word)
        word = "" + digits[i]
​
    container.append(word)
​
  container_sort = container
  container_sort = sorted(container, key = len)
  x = len(container_sort[-1])
  container_sort = []
  for i in range(0, len(container)):
    if len(container[i]) == x:
      container_sort.append(container[i])
​
  return container_sort[0]

