
def letter_combinations(digits):
  phone = {
    "2" : "abc",
    "3" : "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno", 
    "7" : "pqrs", 
    "8" : "tuv", 
    "9" : "wxyz"
  }
​
  comb, digits, trial= [], str(digits), ""
​
  for j in phone[digits[0]]:
    for k in phone[digits[1]]:
      
      if len(digits) == 3: 
        for l in phone[digits[2]]:
          trial += j + k + l
          comb.append(trial)
          trial = ""
​
      else:
        trial += j + k
​
        comb.append(trial)
        trial = ""
    
  return comb

