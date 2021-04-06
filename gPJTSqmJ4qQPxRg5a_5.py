
def func(num):
  string=str(num)
  count=0
  for char in string:
    count+=int(char)
  return count-len(string)*len(string)

