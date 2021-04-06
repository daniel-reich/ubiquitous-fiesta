
def most_frequent_char(lst):
  freq = {l: ''.join(lst).count(l) for l in set(''.join(lst))}
  return sorted([k for k, v in freq.items() if v == max(freq.values())])

