
def count_ones(num):
  string = bin(num)
  count = 0
  for x in range(0,len(string)):
    if string[x] == '1' : count+=1
  return count

