
def letter_counter(lst, letter):
  count = 0
  for l in lst:
    count += l.count(letter)
  return count

