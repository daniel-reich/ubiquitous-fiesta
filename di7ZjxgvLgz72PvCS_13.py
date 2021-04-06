
def validate_swaps(lst, txt):
  results = []
  for word in lst:
    if len(word) != len(txt) or sorted(word) != sorted(txt):
      results.append(999)
      continue  
    mismatches = 0
    for char1, char2 in zip(word, txt):
      if char1 != char2:
        mismatches += 1
    results.append(mismatches)
  
  return [result <= 2 for result in results]

