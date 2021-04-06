
def how_many_times(msg):
  letters='abcdefghijklmnopqrstuvwxyz'
  total=0
  for i in msg:
    total+=letters.find(i)+1
  return total

