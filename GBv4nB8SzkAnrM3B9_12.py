
def letter_counter(lst, letter):
  count = 0
  for arr in lst:
    count += arr.count(letter)
  return count

