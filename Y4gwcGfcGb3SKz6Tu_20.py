
def max_separator(string):
  def find_substrings(s):
    substrings = {}
    l8rs = list(set(s))
   # print(l8rs)
    for l8r in l8rs:
      count = s.count(l8r)
      indexes = []
    #  print(l8r, count)
      for n in range(len(s)):
        if s[n] == l8r:
          indexes.append(n)
     # print(indexes)
      substrings[l8r] = [indexes[n+1] - indexes[n] for n in range(len(indexes)-1)]
    
    return substrings
  
  fs = find_substrings(string)
​
  max_substring = 0
  max_l8r = []
​
  for l8r in fs:
    try:
      if max(fs[l8r]) > max_substring:
        max_substring = max(fs[l8r])
        max_l8r = [l8r]
      elif max(fs[l8r]) == max_substring:
        max_l8r.append(l8r)
    except ValueError:
      continue
​
  return sorted(max_l8r)

