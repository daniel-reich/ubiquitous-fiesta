
def letter_counter(lst, letter):
  return sum(sum(1 for i in j if i==letter) for j in lst)

