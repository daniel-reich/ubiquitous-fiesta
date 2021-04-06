
def get_length(lst):
  def flatter(lst):
    s = str(lst).split(', ')
    nl = []
​
    for item in s:
      if '[' in item:
        item = item.strip('[')
      if ']' in item:
        item = item.strip(']')
      if isinstance(item, str) == True and len(item) == 0:
        continue
      nl.append(item)
    
    return nl
​
​
  if lst == []:
    return 0
  
  else:
    flat = flatter(lst)
    length = len(flat)
​
    return length

