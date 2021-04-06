
def tidy_books(lst):
  result = []
​
  for item in lst:
    for string in item:
      string = string.strip().split(' - ')
      result.append(string)
  
  return result

