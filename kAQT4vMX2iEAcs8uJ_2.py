
def checker(word):
  prohibited = ["k", "m", "v", "w", "x"]
  for letter in word:
    if letter in prohibited:
      return False
  return True
​
​
def longest_7segment_word(lst):
  new_list = []
  for i in lst:
    if checker(i):
      new_list.append(i)
  if len(new_list) == 0:
    return ""
  x = sorted(new_list, key=len, reverse=True)
  return x[0]

