
def average_index(letters):
  total=0
  for i in letters:
    total+=ord(i)-96
  return round(total/len(letters), 2)

