
def is_valid_subsequence(lst, sequence):
  if len(lst)>len(sequence):
    return all(x in lst for x in sequence)
  else:
    return lst==sequence

