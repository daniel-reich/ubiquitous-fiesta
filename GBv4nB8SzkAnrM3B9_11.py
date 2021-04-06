
def letter_counter(lst, letter):
  count = 0
  for i in range(len(lst)):
    for j in lst[i]:
      if j == letter:
        count += 1
  return count

