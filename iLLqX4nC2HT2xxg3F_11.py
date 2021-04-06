
def deepest(lst):
  cur_count = 0
  max_count = 0
  
  for char in str(lst):
    if char == "[":
      cur_count += 1
      if cur_count > max_count:
        max_count = cur_count
    elif char == "]":
      cur_count -= 1
  
  return max_count

