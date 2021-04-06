
def is_valid_subsequence(array, sequence):
  seqindex = 0
  for i in array:
    if seqindex == len(sequence):
         break
    if sequence[seqindex] == i:
      seqindex+=1
  return seqindex == len(sequence)

