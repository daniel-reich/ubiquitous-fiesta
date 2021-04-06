
def sock_merchant(lst):
  
  diff_colors = list(set(lst))
  matched = 0
  
  for color in diff_colors:
    matched += lst.count(color) // 2
  
  return matched

