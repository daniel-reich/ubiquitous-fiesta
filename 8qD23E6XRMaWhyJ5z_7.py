
def happiness_number(s):
  
  sum = 0
  for i in range(len(s)-1):
    if (s[i] == ":" and s[i+1] == ")") or (s[i] == "(" and s[i+1] == ":"):
      sum = sum + 1
    elif (s[i] == ":" and s[i+1] == "(") or (s[i] == ")" and s[i+1] == ":"):
      sum = sum - 1
    else:
      sum = sum + 0
  
  return sum

