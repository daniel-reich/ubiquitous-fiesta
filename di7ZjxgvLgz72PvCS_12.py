
def validate_swaps(lst, txt):
  return [False if diff(word, txt) > 2 else True for word in lst]
      
​
def diff(test_word, ideal_word):
  if len(test_word) != len(ideal_word) or set(test_word) != set(ideal_word):
    return 3
  else:
    count = 0
    for a in range(len(test_word)):
      if test_word[a] != ideal_word[a]:
        count += 1
      if count > 2:
        return count
    return count

