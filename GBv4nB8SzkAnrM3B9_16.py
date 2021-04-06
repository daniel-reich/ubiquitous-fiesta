
def letter_counter(lst, letter):
  return sum([1 for x in lst for y in x if y == letter])

