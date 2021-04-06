
def tidy_books(lst):  
  arr = []
​
  for s in lst:
    line = s[0]
    line = ' '.join(line.split())
    line = line.lstrip()
    line = line.rstrip()
    line_list = line.split(' - ')
​
    arr.append(line_list)
​
  return(arr)

