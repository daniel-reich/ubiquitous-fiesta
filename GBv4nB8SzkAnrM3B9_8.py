
def letter_counter(lst, letter):
  count=0
  for i in lst:
    for x in i:
      if x==letter: count+=1
  return count

