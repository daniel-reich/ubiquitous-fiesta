
def covered_integers(lst):
  numbers = []
  for i in lst:
    for n in range(i[0], i[1]+1):
      numbers.append(n)
  return len(set(numbers))

