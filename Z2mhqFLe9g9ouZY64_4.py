
def is_valid_subsequence(lst, sequence):
  lst = list(filter(lambda x: x in sequence,lst))
  if any(x not in lst for x in sequence):
    return False
  if lst == sequence:
    return True
  return is_valid_subsequence(lst[lst.index(sequence[0])+1::],sequence[1::])

