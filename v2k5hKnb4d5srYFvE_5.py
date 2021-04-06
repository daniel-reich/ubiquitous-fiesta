
def letters_combinations(digits):
  
  if len(digits) == 0:
    return set()
    
  d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
  
  start_list = lambda digit: [d[digit][n] for n in range(len(d[digit]))]
  advance_list = lambda list, digit: [l8r + d[digit][n] for l8r in list for n in range(len(d[digit]))]
  
  lst = start_list(digits[0])
  
  for digit in digits[1:]:
    lst = advance_list(lst, digit)
  
  return set(lst)

