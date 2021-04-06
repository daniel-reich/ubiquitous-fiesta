
d = { "":"", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
​
def letters_combinations(digits):
  if len(digits)<2:return set(d[digits])
  return set(\
    [x+y for x in d[digits[0]] \
    for y in letters_combinations(digits[1:])] \
    )

