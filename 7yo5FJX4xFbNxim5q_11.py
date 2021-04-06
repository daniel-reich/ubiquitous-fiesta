
def harry(po):
  letter_count = 0
  letter_count_alt = 0
  po_length = len(po)
  last_po_length = len(po[po_length-1])   
  if po_length == 1 and last_po_length == 0:
    return -1
  elif po_length == 1:
    return sum(po[0])
  else:
    for i in range(po_length-1):
      letter_count = letter_count + po[i][0]
    for j in range(last_po_length):
      letter_count = letter_count + po[last_po_length-1][j]
    for j in range(last_po_length-1):
      letter_count_alt = letter_count_alt + po[0][j]
    for i in range(po_length):
      letter_count_alt = letter_count_alt + po[i][last_po_length-1]
    return max(letter_count, letter_count_alt)

