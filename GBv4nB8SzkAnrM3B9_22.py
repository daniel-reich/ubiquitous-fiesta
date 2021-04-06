
def letter_counter(lst, letter):
  count_l = 0
  for lstElem in lst:
    for x in lstElem:
        if x == letter:
          count_l += 1
  return count_l

