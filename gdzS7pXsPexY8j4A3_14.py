
def count_digits(lst, t):
  counts = []
  for num in lst:
    if t=='odd':
      count = len(list(filter(lambda x:x%2, [int(d) for d in str(num)])))
    elif t=='even':
      count = len(list(filter(lambda x:x%2==0, [int(d) for d in str(num)])))
    counts.append(count)
  return counts

