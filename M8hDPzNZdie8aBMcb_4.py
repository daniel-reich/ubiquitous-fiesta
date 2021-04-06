
def count_substring(s):
  n = []
  for i in range(len(s)):
    
    for j in range(len(s)):
      if j > i:
        n.append(s[i:j+1])
​
  return  len([i  for i in n if i[0] == "A" and i[-1] == "X" ])

