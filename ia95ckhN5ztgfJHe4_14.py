
def comments_correct(txt):
  if len(txt) % 2: return False
​
  split = [txt[i:i+2] for i in range(0,len(txt)-1, 2)]
  if any(item not in ['//', '/*', '*/'] for item in split): return False
  if any(split[i+1] != '*/' for i in range(len(split)-1) if split[i] == '/*'): return False
  
  return True

