
def letter_counter(lst, letter):
  return sum(row.count(letter) for row in lst)

