
def number_of_swaps(lst):
  i = swap_count = 0
  while i+1!= len(lst):
    if lst[i] > lst[i+1]: 
      lst[i] ^= lst[i+1]
      lst[i+1] ^= lst[i]
      lst[i] ^= lst[i+1]
      swap_count += 1
      i = 0
    else: i += 1
  return swap_count

