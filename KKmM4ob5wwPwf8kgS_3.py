
def get_frequencies(lst):
  freq = {}
  for i in lst:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1
  return freq

