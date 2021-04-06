
def letter_counter(lst, letter):
  count = 0
  for x in lst:
    count += x.count(letter)
  return count

