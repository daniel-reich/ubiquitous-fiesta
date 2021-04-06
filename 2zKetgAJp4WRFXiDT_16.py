
def number_length(num):
  count = 0
  for x in str(num):
    list(str(num)).pop()
    count+=1
  return count

